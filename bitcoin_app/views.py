# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import Bitcoin


def index(request):
    price = Bitcoin.get_current_price()
    average = Bitcoin.get_average_price_last_10min()
    last_10_min = Bitcoin.get_last_10min_time_min_max()

    context = {'price': price, 'average': average, 'last_10_min': last_10_min}
    return render(request, 'bitcoin_app/index.html', context=context)
