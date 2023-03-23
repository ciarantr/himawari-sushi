from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccess.as_view(),
         name='contact_success'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('reservations/', views.Reservations.as_view(), name='reservations'),
    path('subscribe-success/', views.SubscribeSuccess.as_view(),
         name='subscribe_success'),
]
