# -*- coding: utf-8 -*-

import signal
import time

from django.core.management.base import BaseCommand
from bitcoin_app.models import bitcoinDataManager


class Command(BaseCommand):
    def handle(self, **options):

        signal.signal(signal.SIGTERM, bitcoinDataManager.service_shutdown)
        signal.signal(signal.SIGINT, bitcoinDataManager.service_shutdown)

        try:
            get_bitcoin = bitcoinDataManager.GetBitcoinThread()
            erase_bitcoin = bitcoinDataManager.EraseOldBitcoinThread()
            get_bitcoin.start()
            erase_bitcoin.start()
            while True:
                time.sleep(0.01)

        except bitcoinDataManager.ServiceExit:
            get_bitcoin.shutdown_flag.set()
            erase_bitcoin.shutdown_flag.set()
            get_bitcoin.join()
            erase_bitcoin.join()

