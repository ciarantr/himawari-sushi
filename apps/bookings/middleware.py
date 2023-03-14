import uuid

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from apps.bookings.models import Booking


class BookingMiddleware:
    # A middleware class to check if a user is
    # trying to edit a booking that is not theirs
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.path.startswith('/booking/edit/') \
                or request.path.startswith('/booking/delete/'):

            if not request.user.is_authenticated:
                messages.error(request,
                               'You must be logged in to edit a booking.')
                return redirect(reverse('login'))

            booking_id = view_kwargs['pk']
            # return 404 if booking_id does not exist not valid uuid
            try:
                uuid.UUID(booking_id)
            except ValueError:
                raise Http404

            booking = get_object_or_404(Booking, pk=booking_id)
            user = User.objects.get(username=request.user)

            if booking.customer_id != user.id:
                messages.error(request,
                               'You do not have permission'
                               ' to edit this booking.')
                return redirect(reverse('profile-bookings'))

        return None
