from django.test import TestCase
from django.urls import reverse


class TestMenuView(TestCase):

    def test_menu_view(self):
        """
        Test the view is rendered correctly using the
        template menu.html
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')
