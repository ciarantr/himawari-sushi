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

    def test_can_create_booking(self):
        # Create a booking
        response = self.client.post(self.booking_create_url, {
            'booking_date': today_date,
            'booking_time': '13:00',
            'placements': '2',
            'message': 'Test booking message',
        })
        # Check if booking was created and redirect to profile page
        self.assertRedirects(response, self.profile_url)
        self.assertEquals(Booking.objects.count(), 1)
        self.assertEquals(
            Booking.objects.get().booking_date, today_date)
        self.assertEquals(Booking.objects.get().booking_time.strftime('%H:%M'),
                          '13:00')
        self.assertEquals(Booking.objects.get().placements, 2)
        self.assertEquals(Booking.objects.get().message, 'Test booking message')
        self.assertEquals(Booking.objects.get().customer, self.customer)

    def test_can_edit_booking(self):
        # Create a booking
        response = self.client.post(self.booking_create_url, {
            'booking_date': today_date,
            'booking_time': '13:00',
            'placements': '2',
            'message': 'Test booking message',

        })
        # Get the booking by customer and date
        booking_pk = Booking.objects.get(
            customer=self.customer,
            booking_date=today_date
        ).pk
        # Get the date for tomorrow
        tomorrow_date = date.today() + timedelta(days=1)
        # Edit the booking and add the pk to the url
        response = self.client.post(
            self.booking_edit_url.replace('1', str(booking_pk)), {
                'booking_date': tomorrow_date,
                'booking_time': '14:00',
                'placements': '5',
                'message': 'Test booking message changed',
            }
        )

        # Check if booking was edited with the new values
        self.assertRedirects(response, self.profile_url)
        self.assertEquals(
            Booking.objects.get().booking_date,
            tomorrow_date)
        self.assertEquals(Booking.objects.get().booking_time.strftime('%H:%M'),
                          '14:00')
        self.assertEquals(Booking.objects.get().placements, 5)
        self.assertEquals(Booking.objects.get().message,
                          'Test booking message changed')
        self.assertEquals(Booking.objects.get().customer, self.customer)
