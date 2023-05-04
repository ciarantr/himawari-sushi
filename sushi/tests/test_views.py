from django.test import SimpleTestCase

# TODO: Need to add tests for the 404 500 Templates
#  place the following in the view to raise a 500 error
# raise Exception("500 error") and comment out line 20 to test the 500 page
# test the 404 and 500 error pages


class CustomErrorHandlerTests(SimpleTestCase):

    def test_404_error_page(self):
        response = self.client.get('/404/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')

    def test_500_error_page(self):
        response = self.client.get('/500/')
        self.assertRaises(Exception, response.status_code, 500)
        # self.assertTemplateUsed(response, 'errors/500.html')