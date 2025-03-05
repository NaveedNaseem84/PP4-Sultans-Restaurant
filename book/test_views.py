from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import MakeBooking


class CreateBookingTestCase(TestCase):

    def setUp(self):
        """
        Set up a test user who has then
        logged in.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testp4ssw0rd"
            )
        self.client.login(username="testuser", password="testp4ssw0rd")

    def test_create_booking_valid(self):
        """
        Test a valid booking is created successfully.
        """

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': '04/03/2025',
            'time_slot': '5.30',
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        
        self.assertIn('booking created.', messages)
        self.assertEqual(response.status_code, 302)

    def test_create_booking_date_past_date(self):
        """
        Test if the requested date is in the past,
        returns an error via messages.
        """

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': '01/03/2025',
            'time_slot': '7.30',
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You can only book from today onwards!', messages)

    def test_create_duplicate_booking(self):
        """
        Test to see if a booking already exists with the same time as
        the posted date/time already exits.
        If so returns an error.
        """
        existing_booking_date = '2025-03-04'
        existing_booking_time = '7.30'

        MakeBooking.objects.create(
            user=self.user,
            name=self.user.username,
            email='test@me.com',
            phone='01212490141',
            date=existing_booking_date,
            time_slot=existing_booking_time,
            number_of_people='6',
            special_requests='Birthday'
        )

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': existing_booking_date,
            'time_slot': existing_booking_time,
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Sorry, time slot unavailable on this date.', messages)
