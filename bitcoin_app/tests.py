# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.utils import timezone
from .models import Bitcoin


class TestPages(TestCase):
    def setUp(self):
        for i in range(3, 600, 5):
            Bitcoin.objects.create(
                price=i,
                time=timezone.now() - timezone.timedelta(seconds=i),
            )

    def test_index_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_current_price(self):
        numbers = range(3, 600, 5)
        current_price = numbers[0]
        client = Client()
        response = client.get('/')
        self.assertContains(response, current_price)

    def test_avg_price(self):
        numbers = range(3, 600, 5)
        avg_price = sum(numbers) / len(numbers)
        client = Client()
        response = client.get('/')
        self.assertContains(response, avg_price)

    def test_min_prices(self):
        numbers = range(3, 600, 5)
        client = Client()
        response = client.get('/')
        for i in range(10):
            min_price = min(numbers[i*12:i*12+12])
            self.assertContains(response, min_price)

    def test_max_prices(self):
        numbers = range(3, 600, 5)
        client = Client()
        response = client.get('/')
        for i in range(10):
            min_price = max(numbers[i*12:i*12+12])
            self.assertContains(response, min_price)

