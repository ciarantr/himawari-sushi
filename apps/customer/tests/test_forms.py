from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import CustomerUpdateForm
from ..models import Customer


class TestForms(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            customer=User.objects.create_user(
                username='testuser',
                password='testpassword',
            )
        )

    def test_pass_customer_update_form(self):
        form = CustomerUpdateForm(data={
            'username': 'testuser2',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '1234567890'

        })
        self.assertTrue(form.is_valid())

    def test_fail_customer_update_username_exists(self):
        form = CustomerUpdateForm(data={
            'username': 'testuser'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['username'][0],
                          'A user with that username already exists.')

