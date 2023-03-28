from datetime import date, timedelta

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Booking
from ..models import Customer

today_date = date.today()


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile-bookings')
        self.booking_create_url = reverse('booking_create')
        self.booking_delete_url = reverse('booking_delete', args=[1])
        self.booking_edit_url = reverse('booking_edit', args=[1])

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.customer = Customer.objects.create(
            customer=self.user
        )
        # login the user
        self.client.login(username='testuser', password='testpassword')

    def test_GET_booking_page(self):
        response = self.client.get(self.booking_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking.html')