from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.email = "test@gmail.com"
        self.password = "testpassword"
        self.password2 = "testpassword"

        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_GET_login(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


