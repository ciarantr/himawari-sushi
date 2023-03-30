from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Customer


class TestViews(TestCase):

    def setUp(self):
        self.new_customer = Customer.objects.create(
            customer=User.objects.create_user(
                username='testuser',
                password='testpassword',
            )
        )
        # get customer by username
        self.customer = Customer.objects.get(customer__username='testuser')
        self.client.login(username='testuser', password='testpassword')

    def test_GET_customer_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/index.html')

    def test_GET_customer_profile_bookings_page(self):
        response = self.client.get(reverse('profile-bookings'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/bookings.html')

    def test_GET_customer_profile_edit_page(self):
        response = self.client.get(reverse('profile-details'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/account.html')

    def test_POST_customer_profile_edit_page(self):
        response = self.client.post(reverse('profile-details'), {
            'username': 'Cal',
            'first_name': 'Callum',
            'last_name': 'Peterson',
            'email': 'newemail@gmail.com',
            'phone_number': '656565632'
        })
        # refresh customer object
        self.customer.refresh_from_db()
        # check if customer details are updated
        self.assertEquals(self.customer.customer.username, 'Cal')
        self.assertEquals(self.customer.customer.first_name, 'Callum')
        self.assertEquals(self.customer.customer.last_name, 'Peterson')
        self.assertEquals(self.customer.customer.email, 'newemail@gmail.com')
        self.assertEquals(self.customer.phone_number, '656565632')
        # check if redirect to profile page
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('profile-details'))
