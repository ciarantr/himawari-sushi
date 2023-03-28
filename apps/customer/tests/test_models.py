from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Customer


class TestCustomerModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.customer = Customer.objects.create(customer=self.user,
                                                phone_number='772121')

    def test_customer_model(self):
        # check if customer is created and has correct attributes
        self.assertEqual(self.customer.customer, self.user)
        self.assertEqual(self.customer.phone_number, '772121')
        self.assertEqual(self.customer.customer.username, 'testuser')
