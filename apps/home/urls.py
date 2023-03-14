from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccess.as_view(),
         name='contact_success'),
]
