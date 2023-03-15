from . import views
from django.urls import path

urlpatterns = [
    path('profile/dashboard/', views.CustomerDashboard.as_view(),
         name='profile'),
    path('profile/dashboard/my-bookings/', views.CustomerBookings.as_view(),
         name='profile-bookings'),
    path('profile/dashboard/my-details/', views.CustomerProfile.as_view(),
         name='profile-details'),
]
