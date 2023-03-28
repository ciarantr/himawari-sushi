from django.test import SimpleTestCase
from django.urls import resolve, reverse

from apps.accounts.views import LoginUser, LogoutUser, CreateUser


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginUser)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutUser)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, CreateUser)
