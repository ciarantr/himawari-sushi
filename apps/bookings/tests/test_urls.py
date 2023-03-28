from django.test import SimpleTestCase
from django.urls import resolve, reverse

from apps.bookings.views import BookingCreate, BookingEdit, BookingDelete


class TestUrls(SimpleTestCase):

    def test_booking_create_url_is_resolved(self):
        url = reverse('booking_create')
        self.assertEquals(resolve(url).func.view_class, BookingCreate)

    def test_booking_edit_url_is_resolved(self):
        url = reverse('booking_edit', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookingEdit)

    def test_booking_delete_url_is_resolved(self):
        url = reverse('booking_delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookingDelete)
