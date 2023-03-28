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

