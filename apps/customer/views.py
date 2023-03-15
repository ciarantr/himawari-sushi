from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from apps.bookings.models import Booking


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


        return render(request, template, context)

