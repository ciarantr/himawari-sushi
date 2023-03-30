from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import Home, About, Contact, ContactSuccess, Menu, Reservations, \
    SubscribeSuccess


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func.view_class, About)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, Contact)

    def test_contact_success_url_is_resolved(self):
        url = reverse('contact_success')
        self.assertEquals(resolve(url).func.view_class, ContactSuccess)

    def test_menu_url_is_resolved(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func.view_class, Menu)

    def test_reservations_url_is_resolved(self):
        url = reverse('reservations')
        self.assertEquals(resolve(url).func.view_class, Reservations)

    def test_subscribe_success_url_is_resolved(self):
        url = reverse('subscribe_success')
        self.assertEquals(resolve(url).func.view_class, SubscribeSuccess)
