from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import time, date


def booking_date_validator(booking_date) -> str or None:
    # Validate booking date is today or not pas end of year
    if booking_date < date.today():
        raise ValidationError(
            _(
                'Please select a date from today onwards'
            )
        )
    elif booking_date > date(date.today().year, 12, 31):
        raise ValidationError(
            _(
                'We can only accept bookings up to the end of the year'
            )
        )


def booking_time_validator(booking_time) -> str or None:
    # Validate booking time is between 13:00 and 21:00
    if booking_time < time(13, 00) or booking_time > time(21, 00):
        raise ValidationError(
            _(
                'Please select a time between 13:00 p.m and 21:00 p.m'
            )
        )


def booking_placement_validator(booking_placements) -> str or None:
    # Validate placements is between 1 and 20
    if booking_placements < 1:
        raise ValidationError(
            _(
                'You need to book at least 1 placement'
            )
        )
    elif booking_placements > 20:
        raise ValidationError(
            _(
                'You can only book up to 20 placements'
            )
        )
