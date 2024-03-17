import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductsFactory

from order.factories import UserFactory, OrderFactory
from product.models import Products
from order.models import Order

class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='techology')
        self.product  = ProductsFactory(title = 'mouse', price = 100, category = [self.category])
        self.order    = OrderFactory(product = [self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', kwargs={'version': '1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data['products'][0]['title'], self.product.title)
        self.assertEqual(order_data['products'][0]['price'], self.product.price)
        self.assertEqual(order_data['products'][0]['category'][0]['title'], self.category.title)
    
    def test_create_order(self):
        user = UserFactory()
        product = ProductsFactory()
        data = json.dumps({
            'products_id': [product.id],
            'user'       : user.id
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': '1'}),
            data = data, 
            content_type= 'application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        create_order= Order.objects.get(user=user)