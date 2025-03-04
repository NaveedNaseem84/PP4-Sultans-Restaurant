from django.test import TestCase
from .forms import BookingForm
# Create your tests here.


class TestBookingForm(TestCase):
    """
    Testing of the booking for validation
    and correct format.
    """

    def test_form_is_valid(self):
        """
        Test a complete valid form.
        """
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

    def test_email_invalid(self):
        """
        Test to validate 'email' field format.
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': '01212490141',
                'date': '04/03/2025',
                'time_slot': '5.30',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="Invalid email format")

    def test_phone_missing(self):
        """
        test 'phone' field for empty value
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': '',
                'date': '04/03/2025',
                'time_slot': '5.30',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="phone required")

    def test_phone_invalid(self):
        """
        Test 'phone' field format.
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': 'sdsddsd',
                'date': '04/03/2025',
                'time_slot': '5.30',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="phone invalid")

    def test_date_missing(self):
        """
        Test 'date' field for empty value.
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': '01212490141',
                'date': '',
                'time_slot': '5.30',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="date required")

    def test_time_slot_missing(self):
        """
        Test 'timeslot' field for empty value.
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': '01212490141',
                'date': '04/03/2025',
                'time_slot': '',
                'number_of_people': '6',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="time slot required")

    def test_no_of_people_missing(self):
        """
        Test 'number of people' fielf for empty value.
        """
        booking_form = BookingForm(
            {
                'email': 'testme.com',
                'phone': '01212490141',
                'date': '04/03/2025',
                'time_slot': '',
                'number_of_people': '',
                'special_requests': 'Birthday'
             })
        self.assertFalse(booking_form.is_valid(), msg="no of people required")
