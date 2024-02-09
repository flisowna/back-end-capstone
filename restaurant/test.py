from django.test import TestCase
from .models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=10.00, inventory=50)
        Menu.objects.create(title="Burger", price=5.00, inventory=100)
        Menu.objects.create(title="Ice Cream", price=2.50, inventory=200)
    
    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data matches expected data
        expected_data = [
            {"title": "Pizza", "price": "10.00", "inventory": 50},
            {"title": "Burger", "price": "5.00", "inventory": 100},
            {"title": "Ice Cream", "price": "2.50", "inventory": 200},
        ]
        for i, menu in enumerate(response.data):
            self.assertEqual(menu['title'], expected_data[i]['title'])
            self.assertEqual(str(menu['price']), expected_data[i]['price'])  # Prices might be returned as strings
            self.assertEqual(menu['inventory'], expected_data[i]['inventory'])