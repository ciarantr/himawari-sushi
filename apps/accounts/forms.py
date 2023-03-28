from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, EmailInput
from django.utils.translation import gettext_lazy as _
from ..validators.customer_validators import email_pattern, username_pattern
from ..validators.customer_validators import validate_email
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             validators=[validate_email], max_length=100)

    email.widget.attrs.update({
        'pattern': email_pattern['pattern'],
        'title': email_pattern['message'],
    })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        labels = {
            'username': _('User name'),
            'password1': _('Password'),
            'password2': _('Password confirmation'),
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

        widgets = {
            'username': TextInput(attrs={'pattern': username_pattern['pattern'],
                                         'title': username_pattern['message'],
                                         }),
        }
