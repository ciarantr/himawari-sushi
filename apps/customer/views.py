from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from apps.bookings.models import Booking
from .forms import CustomerUpdateForm


# Create your views here.

def booking_request(template, request) -> render:
    # A function to query the bookings table for the current user
    # and return the results to the template

    user = User.objects.get(username=request.user)
    # query user's bookings
    # check if the user has a customer profile
    if hasattr(user, 'customer'):
        # query the bookings table for all bookings with the current user
        bookings = Booking.get_booking_information(user)
    else:
        bookings = None

    context = {'bookings': bookings}

    return render(request, template, context)


class CustomerDashboard(View):
    # A view to display the customer's bookings overview
    def get(self, request):
        return booking_request('profile/index.html', request)


class CustomerBookings(View):
    # A view to display the customer's booking details

    def get(self, request):
        return booking_request('profile/bookings.html', request)


class CustomerProfile(View):
    # A class based view for the customer details page
    def get(self, request):

        customer = User.objects.get(username=request.user)
        form = CustomerUpdateForm(instance=customer)
        context = {'form': form,
                   'form_title': 'Your Details',
                   'form_class': 'base-form',
                   'form_id': 'customer-form',
                   'submit_text': 'Update',
                   }
        template = 'profile/account.html'

        return render(request, template, context)

    def post(self, request):

        customer = User.objects.get(username=request.user)
        form = CustomerUpdateForm(request.POST, instance=customer)
        # check if user sent email address in upper case
        # if so, change to lower case

        if form.is_valid() and form.has_changed():
            # change the user's email address to lower case then save
            form.save(commit=False)
            form.instance.email = form.instance.email.lower()
            form.save()

            messages.success(request, 'Your details have been updated.')
            return redirect('profile-details')

        elif not form.has_changed():
            messages.error(request, 'No changes were made.')
            return redirect('profile-details')

        else:
            messages.error(request, 'Please correct the errors below.')
            form = CustomerUpdateForm(data=request.POST, instance=customer)
            context = {'form': form,
                       'form_title': 'Your Details',
                       'form_class': 'base-form',
                       'form_id': 'customer-form',
                       'submit_text': 'Update',
                       }
            return render(request, 'profile/account.html', context)
