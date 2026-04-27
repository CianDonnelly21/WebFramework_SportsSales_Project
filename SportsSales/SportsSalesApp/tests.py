from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, Order, OrderItem

# Create your tests here.
class ItemModelTest(TestCase):
    def test_create_item(self):
        item = Item.objects.create(item_id = 1, name = 'Football', price = 10.0, description = 'Test Item')
        self.assertEqual(item.name, 'Football')

class OrderTest(TestCase):
    def test_create_order(self):
        user = User.objects.create_user(username = 'user1', password = 'password')
        order = Order.objects.create(order_id = 1, user = user, date = '2026-04-07', status = 'Pending')
        self.assertEqual(order.user.username, 'user1')

class LoginTest(TestCase):
    def test_login(self):
        User.objects.create_user(username = 'user1', password = 'password')
        login = self.client.login(username = 'user1', password = 'password')
        self.assertTrue(login)

class OrderUserTest(TestCase):
    def test_order_has_user(self):
        user = User.objects.create_user(username = 'user1', password = 'password')

        order = Order.objects.create(order_id = 1, user = user, date = '2026-04-07', status = 'Pending')
        self.assertEqual(order.user.username, 'user1')