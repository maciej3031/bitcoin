# -*- coding: utf-8 -*-

import signal
import time

from django.core.management.base import BaseCommand
from bitcoin_app.models import GetBitcoinThread, EraseOldBitcoinThread, ServiceExit, service_shutdown


class Command(BaseCommand):
    def handle(self, **options):

        signal.signal(signal.SIGTERM, service_shutdown)
        signal.signal(signal.SIGINT, service_shutdown)

        try:
            get_bitcoin = GetBitcoinThread()
            erase_bitcoin = EraseOldBitcoinThread()
            get_bitcoin.start()
            erase_bitcoin.start()
            while True:
                time.sleep(0.01)

        except ServiceExit:
            get_bitcoin.shutdown_flag.set()
            erase_bitcoin.shutdown_flag.set()
            get_bitcoin.join()
            erase_bitcoin.join()

