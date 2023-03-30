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
