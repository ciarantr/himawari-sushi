from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from apps.bookings.models import Booking


# Create your views here.

class CustomerDashboard(View):
    # A view to display the customer's bookings
    def get(self, request):
        user = User.objects.get(username=request.user)
        # query user's bookings
        # check if the user has a customer profile
        if hasattr(user, 'customer'):
            # query the bookings table for all bookings with the current user
            bookings = Booking.get_booking_information(user)
        else:
            bookings = None

        context = {'bookings': bookings}
        template = 'profile/index.html'
        return render(request, template, context)

