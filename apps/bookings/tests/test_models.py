from django.test import TestCase
from ..models import Booking
from ..models import Customer
from datetime import date
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            customer=User.objects.create_user(
                username='testuser',
                password='testpassword',
            )
        )

    def test_booking_created(self):
        Booking.objects.create(
            customer=self.customer,
            booking_date=date.today(),
            booking_time='13:00',
            placements=2,
            message='Test booking message',
        )
        self.assertEquals(Booking.objects.count(), 1)
        self.assertEquals(
            Booking.objects.get().booking_date,
            date.today())
        self.assertEquals(
            Booking.objects.get().booking_time.strftime('%H:%M'),
            '13:00'
        )
        self.assertEquals(Booking.objects.get().placements, 2)
        self.assertEquals(Booking.objects.get().message,
                          'Test booking message')
        self.assertEquals(Booking.objects.get().customer, self.customer)
