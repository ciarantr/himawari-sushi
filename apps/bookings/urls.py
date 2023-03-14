from . import views
from django.urls import path

urlpatterns = [
    path('booking/create/', views.BookingCreate.as_view(),
         name='booking_create'),
]
