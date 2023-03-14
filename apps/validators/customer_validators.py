from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

name_part_pattern: dict[str, str] = {
    'pattern': '[a-zA-Z]{3,50}',
    'title': 'Name must be 3 to 50 characters long'
             ' and can contain only letters'
}

name_full_pattern: dict[str, str] = {
    'pattern': '[a-zA-Z ]{3,50}',
    'title': 'Name must be 3 to 50 characters'
             ' and can contain only letters and spaces'
}

username_pattern: dict[str, str] = {
    'pattern': '[\w@.+-]{3,100}',
    'title': 'Username must be 3 to 100 characters long and can contain only '
             'letters, numbers and the following special characters: @.+-_'
}
email_pattern: dict[str, str] = {
    'pattern': '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,20}',
    'title': 'Please enter a valid email address e.g. john@gmail.com'
}

phone_number_pattern: dict[str, str] = {
    'pattern': '\+?\d{7,20}',
    'title': "Phone number must be entered in the format: "
             "'8773214 or +8773214'. "
             "Up to 20 digits allowed."
}

message_pattern: dict[dict:int, str] = {
    'pattern': {
        'minlength': 20,
        'maxlength': 500
    },
    'title': 'Please enter a message between 20 and 500 characters'
}


def validate_part_name(name: str) -> str or None:
    # Check if name is between 3 and 50 characters
    name_regex = RegexValidator(
        regex=r'^[a-zA-Z]{3,50}$',
        message=_(
            'Name must be at least 3 characters and '
            'can contain only letters'
        ))

    name_regex(name)


def validate_full_name(name: str) -> str or None:
    # Check if name is between 3 and 50 characters and can contain only letters
    # and spaces
    name_regex = RegexValidator(
        regex=r'^[a-zA-Z ]{3,50}$',
        message=_(
            'Name must be at least 3 characters and '
            'can contain only letters and spaces'
        ))

    name_regex(name)


def validate_message(message: str) -> str or None:
    # Check if message is between 20 and 500 characters
    message_regex = RegexValidator(
        regex=r'^.{20,500}$',
        message=_(
            'Please enter a message between 20 '
            'and 500 characters'))

    message_regex(message)


def validate_email(email: str) -> str or None:
    email_regex = RegexValidator(
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,}$",
        message=_(
            'Please enter a valid email address'
            ' e.g. john@gmail.com'
        ))

    email_regex(email)


def validate_phone_number(value: str) -> str or None:
    #  Check if phone number is between 7 and 20 digits
    phone_regex = RegexValidator(
        regex=r'^\+?\d{7,20}$',
        message=_(
            "Phone number must be entered in the "
            "format: '8773214 or +8773214'. "
            "Up to 20 digits allowed."
        ))

    phone_regex(value)
