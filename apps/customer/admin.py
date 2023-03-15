from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import User


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    @admin.display(description='Name')
    def customer_name(self, obj):
        if obj.customer.first_name and obj.customer.last_name:
            return obj.customer.first_name + " " + obj.customer.last_name
        else:
            return None

    @admin.display(description='Email')
    def customer_email(self, obj):
        if obj.customer.email:
            return obj.customer.email
        else:
            return None

    # set readonly fields
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['customer', 'customer_name', 'customer_email']
        else:
            return []

    # set order of fields
    def get_fields(self, request, obj=None):
        if obj:
            return ['customer', 'customer_name', 'customer_email',
                    'phone_number']
        else:
            return ['customer', 'phone_number']

    # filter out customers that already have a customer profile
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(
                customer__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
        'customer', 'customer_name', 'customer_email', 'phone_number')

    list_filter = ('customer',)
    search_fields = ('customer__username', 'customer__first_name',
                     'customer__last_name', 'customer__email',
                     'phone_number')
