from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from datetime import date, timedelta
from .models import MakeBooking


class CreateBookingTestCase(TestCase):

    def setUp(self):
        """
        1. Set up a test user who has then
        logged in.
        2. Create booking instance for tests.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testp4ssw0rd"
            )
        self.client.login(username="testuser", password="testp4ssw0rd")

        self.existing_booking_date = date.today()
        self.existing_booking_time = '7.30'

        self.booking = MakeBooking.objects.create(
            user=self.user,
            name=self.user.username,
            email='test@me.com',
            phone='01212490141',
            date=self.existing_booking_date,
            time_slot=self.existing_booking_time,
            number_of_people='2',
            special_requests='Meal'
        )

    def test_create_booking_valid(self):
        """
        Test to check a valid booking is created successfully.
        """

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': self.existing_booking_date,
            'time_slot': '5.30',
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

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
            'date': '2025-03-01',
            'time_slot': '7.30',
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

        self.assertIn('You can only book from today onwards!', messages)

    def test_create_booking_time_date_unavailable(self):
        """
        Test to see if a booking already exists with the same time/date as
        the posted date/time already exits.
        If so returns an error.
        """

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': self.existing_booking_date,
            'time_slot': self.existing_booking_time,
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

        self.assertIn('Sorry, time slot unavailable on this date.', messages)

    def test_update_booking_valid(self):
        """
        Test to update selected booking sucessfully.
        """
        new_booking_date = self.existing_booking_date + timedelta(days=1)
        new_booking_time = '7.30'

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': new_booking_date,
            'time_slot':  new_booking_time,
            'number_of_people': '2',
            'special_requests': 'Suprise meal'
        }

        response = self.client.post(reverse(
            'update_booking',
            args=[self.booking.id]),
            post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

        self.assertIn('Booking successfully updated.', messages)
        self.assertEqual(response.status_code, 302)

    def test_update_booking_unvailable(self):
        """
        Test to see if request to update selected booking time
        and/or date conflicts with a existing booking. If so returns an error.
        """

        post_data = {
            'email': 'test@me.com',
            'phone': '01212490141',
            'date': self.existing_booking_date,
            'time_slot': self.existing_booking_time,
            'number_of_people': '6',
            'special_requests': 'Birthday'
        }

        response = self.client.post(reverse('create_booking'), post_data)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

        self.assertIn('Sorry, time slot unavailable on this date.', messages)

    def test_delete_booking(self):
        """
        test to delete selected booking sucessfully.
        """
        response = self.client.post(reverse(
            'delete_booking',
            args=[self.booking.id]))

        messages = [m.message for m in get_messages(response.wsgi_request)]
        for message in messages:
            print(message)

        self.assertIn('Booking Deleted.', messages)
        self.assertEqual(response.status_code, 302)
