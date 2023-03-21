import uuid

from django.db import models

from apps.customer.models import Customer
from ..validators.booking_validators import *
from ..validators.customer_validators import validate_message


# Create your models here.

class Booking(models.Model):
    # A model for a creating a booking

    """
    Customer: The customer who made the booking(One to One)
    booking_id: The unique id for the booking(Primary Key)
    booking_confirmed: A boolean to confirm if the booking has been confirmed
    (Defaults to False)
    booking_date: The date of the booking
    (Validated by booking_date_validator)
    booking_time: The time of the booking (Validated by booking_time_validator)
    created_on: The date the booking was created (Auto_now)
    message: A message from the customer to the restaurant (Optional)
    placements: The number of people in the booking (Defaults to 1)
    """
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False,
                                  unique=True, )
    booking_confirmed = models.BooleanField(default=False)
    booking_date = models.DateField(validators=[booking_date_validator])
    booking_time = models.TimeField(validators=[booking_time_validator])
    created_on = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=500, validators=[validate_message],
                               blank=True, )
    placements = models.PositiveSmallIntegerField(
        default=1,
        validators=
        [booking_placement_validator]
    )

    def __str__(self):
        customer_name = self.customer.customer.first_name + " " + \
                        self.customer.customer.last_name

        customer_email = self.customer.customer.email

        return f"Name {customer_name} | Email {customer_email}"

    def get_booking_information(self) -> list:
        # return booking information for the customer
        bookings = Booking.objects.filter(customer=self.customer)
        booking_information = []

        for booking in bookings:
            booking_information.append({
                'id': booking.booking_id,
                'date': booking.booking_date.strftime('%d/%m/%Y'),
                'time': booking.booking_time.strftime('%H:%M'),
                'confirmed': booking.booking_confirmed,
                'message': booking.message,
                'placements': booking.placements,
            })
        return booking_information
