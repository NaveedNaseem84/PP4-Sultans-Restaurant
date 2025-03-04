from django.test import TestCase
from .forms import BookingForm
# Create your tests here.


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        booking_form = BookingForm(
            {
                'email': 'test@me.com',
                'phone': '01212490141',
                'date': '04/03/2025',
                'time_slot': '5.30',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertTrue(booking_form.is_valid())
