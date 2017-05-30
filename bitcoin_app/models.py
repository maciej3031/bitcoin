# -*- coding: utf-8 -*-

import threading
import time

import GDAX
from django.db import models
from django.db.models import Max, Min, Avg
from django.utils import timezone


class Bitcoin(models.Model):
    price = models.DecimalField('Price', decimal_places=2, max_digits=7)
    time = models.DateTimeField('Time')

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = "Bitcoin"
        verbose_name_plural = "Bitcoins"

    @classmethod
    def get_average_price_last_10min(cls):

        price = Bitcoin.objects.order_by('-time').filter(time__gte=timezone.now() - timezone.timedelta(minutes=10))\
            .aggregate(Avg('price'))
        return price

    @classmethod
    def get_current_price(cls):
        price = cls.objects.order_by('-time').first()
        return price

    @classmethod
    def get_last_10min_time_min_max(cls):
        time_min_max = []
        for i in range(10):
            bitcoin_min_period = cls.objects.order_by('-time').\
                filter(time__gte=timezone.now() - timezone.timedelta(minutes=i+1),
                       time__lt=timezone.now() - timezone.timedelta(minutes=i))
            value = bitcoin_min_period.aggregate(Max('time'), Min('price'), Max('price'))
            time_min_max.append(value)
        return time_min_max


class GetBitcoinThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self.public_client = GDAX.PublicClient()
        self.name = 'GetBitcoinThread'

    def run(self):
        print('{} started'.format(self.name))

        # Dane pobieramy co 5 sekund
        while not self.shutdown_flag.is_set():
            data = self.public_client.getProduct24HrStats()
            price = float(data['last'])

            bitcoin = Bitcoin(price=price, time=timezone.now())
            bitcoin.save()
            time.sleep(5 - (time.time() % 5))

        print('{} stopped'.format(self.name))


class EraseOldBitcoinThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()
        self.name = 'EraseOldBitcoinThread'

    def run(self):
        print('{} started'.format(self.name))

        # kasujemy rekordy starsze niż 12 min
        while not self.shutdown_flag.is_set():
            Bitcoin.objects.filter(time__lt=timezone.now() - timezone.timedelta(minutes=12)).delete()
            time.sleep(5 - (time.time() % 5))

        print('{} stopped'.format(self.name))


class ServiceExit(Exception):
    pass


def service_shutdown(sig_num, frame):
    print('Caught signal {}'.format(sig_num))
    raise ServiceExit