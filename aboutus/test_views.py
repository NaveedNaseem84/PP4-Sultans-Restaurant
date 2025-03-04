from django.test import TestCase
from django.urls import reverse


class TestAboutUsView(TestCase):

    def test_about_us_view(self):
        """
        Test the view is rendered correctly using the
        template about.html
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/about.html')
