from django.test import TestCase
from django.urls import reverse


class TestWelcomePromotionView(TestCase):

    def test_home_view(self):
        """
        Test the view is rendered correctly using the
        template index.html
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/index.html')
