from django.test import TestCase
from ..forms import SignupForm


class TestSignupForm(TestCase):

    def test_pass_signup_form(self):
        form = SignupForm(data={
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertTrue(form.is_valid())

    def test_fail_signup_form_all_fields_required(self):
        form = SignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
