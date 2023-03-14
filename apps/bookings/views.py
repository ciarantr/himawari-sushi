# FIXME: WHEN SUPERUSER IS CREATED FROM FROM CLI, IT DOES NOT CREATE A CUSTOMER
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.utils.safestring import mark_safe
from django.views import View

from apps.customer.models import Customer
from .forms import BookingForm


# Create your views here.

class BookingCreate(View):
    # A class based view for creating & viewing a booking
    def get(self, request):

        form = BookingForm()
        context = {'form': form,
                   'form_title': 'Create a booking',
                   'form_class': 'base-form',
                   'form_id': 'booking-form',
                   'submit_text': 'Book',
                   }
        template = 'bookings/booking.html'

        return render(request, template, context)

    def post(self, request):
        # TODO: ADD BOOKING CONFIRMATION EMAIL
        form = BookingForm(request.POST)
        user = User.objects.get(username=request.user)
        # check if user is customer if not create customer
        if hasattr(user, 'customer'):
            pass
        else:
            customer = Customer.objects.create(customer=user)
            customer.save()

        if form.is_valid():
            customer = user.customer
            booking = form.save(commit=False)
            booking.customer = customer
            booking.save()
            username = customer.customer.username
            username = username[:10]

            message = f"Thank you for booking with us, {username}! \n" \
                      f" We will be in touch shortly to confirm your booking."

            # add lines break to message
            message = message.replace('\n', '<br>')

            messages.success(request, mark_safe(message))
            return redirect('profile-bookings')

        else:
            messages.error(request, form.errors)
            return redirect(reverse('booking_create'))
