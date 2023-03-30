from django import forms
from django.contrib.auth.models import User
from ..validators.customer_validators import *


class CustomerUpdateForm(forms.ModelForm):
    # A form for updating the customer details
    # This form inherits from the User model
    # & adds the phone number field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(
                attrs={'pattern': username_pattern['pattern'],
                       'title': username_pattern['message']
                       },
            ),

            'first_name': forms.TextInput(
                attrs={'pattern': name_part_pattern['pattern'],
                       'title': name_part_pattern['message']
                       },
            ),

            'last_name': forms.TextInput(
                attrs={'pattern': name_part_pattern['pattern'],
                       'title': name_part_pattern['message']
                       },
            ),

            'email': forms.EmailInput(
                attrs={'pattern': email_pattern['pattern'],
                       'title': email_pattern['message']
                       },
            ),

        }

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)

        if hasattr(self.instance, 'customer'):
            # add phone number field to form if user has customer object
            self.fields['phone_number'] = forms.CharField(
                label='Phone Number',
                required=False,
                validators=[validate_phone_number],
                max_length=20,
            )
            self.fields[
                'phone_number'].initial = self.instance.customer.phone_number
            self.fields['phone_number'].widget = forms.TextInput(
                attrs={'pattern': phone_number_pattern['pattern'],
                       'title': phone_number_pattern['message']
                       },
            )

        # extent form validators
        self.fields['username'].validators.append(validate_username)
        self.fields['first_name'].validators.append(validate_part_name)
        self.fields['last_name'].validators.append(validate_part_name)
        self.fields['email'].validators.append(validate_email)

    def save(self, commit=True):
        # check if user has customer object and
        # if so, update user & customer info
        user = super(CustomerUpdateForm, self).save(commit=False)
        if hasattr(self.instance, 'customer'):
            user.customer.phone_number = self.cleaned_data['phone_number']
            if commit:
                user.save()
                user.customer.save()
        else:
            if commit:
                user.save()
        return user
