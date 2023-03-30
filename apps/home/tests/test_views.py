from django.test import TestCase
from django.contrib.messages import get_messages


class TestViews(TestCase):

    def test_GET_home_page(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'index.html')

    def test_GET_about_page(self):
        url = self.client.get('/about/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'about.html')

    def test_GET_contact_page(self):
        url = self.client.get('/contact/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'contact.html')

    def test_GET_menu_page(self):
        url = self.client.get('/menu/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'menu.html')

    def test_Get_reservations_page(self):
        url = self.client.get('/reservations/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'reservations.html')

    def test_GET_contact_success_page_redirect(self):
        # middleware prevents direct access without form submission
        url = self.client.get('/contact/success/')
        self.assertEqual(url.status_code, 302)

    def test_GET_subscribe_page(self):
        # middleware prevents direct access without form submission
        url = self.client.get('/subscribe-success/')
        self.assertEqual(url.status_code, 302)

    def test_subscribe_form_success(self):
        response = self.client.post('/', data={
            'email': 'test@gmail.com'
        })
        self.assertRedirects(response, '/subscribe-success/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Success! We will send you your discount soon.'
        )

