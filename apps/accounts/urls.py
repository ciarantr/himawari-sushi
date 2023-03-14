from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('register/', views.CreateUser.as_view(), name='register'),
]
