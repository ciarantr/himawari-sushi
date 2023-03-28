from datetime import datetime
from django.test import TestCase
from ..forms import BookingForm

today_date = datetime.now().strftime('%Y-%m-%d')


class TestBookingForm(TestCase):

    def test_pass_booking_form(self):
        form = BookingForm(data={
            'booking_date': today_date,
            'booking_time': '13:00',
            'placements': '2',
        })
        self.assertTrue(form.is_valid())

    def test_fail_booking_form_no_data(self):
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_fail_booking_form_future_date_out_range(self):
        form = BookingForm(data={
            'booking_date': '2026-01-01',
            'booking_time': '13:00',
            'placements': '2',
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(
            form.errors['booking_date'][0],
            'We can only accept bookings up to the end of the year'
        )

    def test_fail_booking_form_time_out_of_range(self):
        form = BookingForm(data={
            'booking_date': today_date,
            'booking_time': '12:00',
            'placements': '2',
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(
            form.errors['booking_time'][0],
            'Please select a time between 13:00 p.m and 21:00 p.m'
        )
