from django.contrib import admin
from .models import Booking


# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    # set order of fields if editing a booking
    list_display = (
        'customer', 'booking_confirmed', 'booking_id',
        'booking_date', 'booking_time', 'placements', 'message')

    list_ordering = ('-created_on',)
    list_filter = ('booking_date', 'booking_time', 'placements')
    search_fields = ('customer__customer__first_name',
                     'customer__customer__last_name',
                     'customer__customer__email',
                     'customer__customer__username',
                     'booking_id')
    date_hierarchy = 'booking_date'

    # set read only fields if editing a booking
    def get_readonly_fields(self, request, obj=None) -> list:
        if obj:
            return ['customer', 'booking_id', 'created_on']
        else:
            return []

    # set order of fields if creating/viewing a new booking
    def get_fields(self, request, obj=None) -> list:
        if obj:
            return ['customer', 'booking_id', 'booking_confirmed',
                    'booking_date', 'booking_time', 'message', 'placements',
                    'created_on']
        else:
            return ['customer', 'booking_confirmed', 'booking_date',
                    'booking_time', 'message', 'placements']
