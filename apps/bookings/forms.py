from datetime import date, datetime, time, timedelta

from django import forms

from .models import Booking

current_year = datetime.now().year
current_time = datetime.now().time()
today_date = date.today()
tomorrow_date = today_date + timedelta(days=1)

date_today = today_date.strftime('%Y-%m-%d')
date_tomorrow = tomorrow_date.strftime('%Y-%m-%d')
date_end_of_year = date(current_year, 12, 31).strftime('%Y-%m-%d')
booking_time_default = current_time
booking_date_default = date_today

# change the if statement to switch between 15 mins and 30 mins
# change the following if statement to switch between 15 mins and 30 mins

if current_time.minute <= 10:
    # set the booking time to the next half hour
    booking_time_default = time(current_time.hour, 15)

elif current_time.minute <= 20:
    # set the booking time to the next half hour
    booking_time_default = time(current_time.hour, 30)

elif current_time.minute <= 30:
    # set the booking time the current hour and 45 mins
    booking_time_default = time(current_time.hour, 45)

elif current_time.minute > 30:
    # set the booking time to the next hour
    booking_time_default = time(current_time.hour + 1, 00)

# set the booking date to tomorrow at 1pm if past 9pm
if current_time.hour >= 21:
    booking_date_default = date_tomorrow
    booking_time_default = time(13, 00)

# set the booking time to 1pm if before 1pm
if current_time.hour < 13:
    booking_time_default = time(13, 00)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'placements', 'message']

        widgets = {
            'booking_date':
                forms.DateInput(attrs={'type': 'date', 'min': date_today,
                                       'max': date_end_of_year,
                                       'value': booking_date_default}),

            'booking_time':
                forms.TimeInput(
                    attrs={'type': 'time', 'min': '13:00',
                           'max': '21:00', 'step': '900',
                           'value': booking_time_default}),

            'placements': forms.NumberInput(
                attrs={'max': 20, 'value': 1}),

            'message':
                forms.Textarea(
                    attrs={'placeholder': 'special request',
                           'minlength': 20,
                           'maxlength': 500
                           }
                ),
        }

        labels = {'booking_date': 'Booking Date',
                  'booking_time': 'Booking Time',
                  'placements': 'Number of Placements', 'message': 'Message', }

        help_texts = {'booking_date': 'book date', 'booking_time': None,
                      'placements': None, 'message': None, }
