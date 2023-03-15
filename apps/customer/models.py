from django.db import models
from django.contrib.auth.models import User
from ..validators.customer_validators import validate_phone_number


# Create your models here.
class Customer(models.Model):
    # A customer model that extends the default django user model
    """
    A customer model that extends the default django user model
    customer: OneToOneField to the default django user model
    phone_number: CharField to store the customer's phone number
    """
    customer = models.OneToOneField(User, primary_key=True,
                                    on_delete=models.CASCADE,
                                    )
    phone_number = models.CharField(blank=True,
                                    validators=[validate_phone_number],
                                    max_length=20,
                                    )

    def __str__(self):
        return self.customer.username
