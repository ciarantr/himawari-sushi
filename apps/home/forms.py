from django import forms
from ..validators.customer_validators import *


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name',
        max_length=50,
        validators=[validate_full_name],
        widget=forms.TextInput(
            attrs={
                'pattern': name_full_pattern['pattern'],
                'title': name_full_pattern['message']
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        max_length=100,
        validators=[validate_email],
        widget=forms.EmailInput(
            attrs={
                'pattern': email_pattern['pattern'],
                'title': email_pattern['message']
            }
        )
    )

    phone_number = forms.CharField(
        label='Phone Number',
        max_length=20,
        validators=[validate_phone_number],
        widget=forms.TextInput(
            attrs={
                'pattern': phone_number_pattern['pattern'],
                'title': phone_number_pattern['message']
            }
        )
    )

    message = forms.CharField(
        label='Message',
        max_length=500,
        validators=[validate_message],
        widget=forms.Textarea(
            attrs={
                'maxlength': message_pattern['max_length'],
                'minlength': message_pattern['min_length'],
                'title': message_pattern['message']
            }
        )
    )
