from ..forms import ContactForm, SubscribeForm
from django.test import TestCase


class TestForms(TestCase):

    def test_pass_contact_form(self):
        form = ContactForm(data={
            'full_name': 'Test Name',
            'email': 'test@gmail.com',
            'phone_number': '123456789',
            'message': 'Test message longer than 20 characters',
        })
        self.assertTrue(form.is_valid())

