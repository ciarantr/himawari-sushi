from django.test import TestCase

from ..forms import CustomerUpdateForm


class TestForms(TestCase):

    def test_pass_customer_update_form(self):
        form = CustomerUpdateForm(data={
            'username': 'testuser2',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '1234567890'

        })
        self.assertTrue(form.is_valid())
