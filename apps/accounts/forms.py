from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, EmailInput
from django.utils.translation import gettext_lazy as _
from ..validators.customer_validators import email_pattern, username_pattern


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        labels = {
            'username': _('User name'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Password confirmation'),
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

        widgets = {
            'username': TextInput(attrs={'pattern': username_pattern['pattern'],
                                         'title': username_pattern['message'],
                                         }),
            'email': EmailInput(attrs={'pattern': email_pattern['pattern'],
                                       'title': email_pattern['message'],
                                       }),
        }
