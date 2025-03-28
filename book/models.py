"""
Import of libraries
"""
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


TIME_SLOTS = [
    ("5.30", "5.30"),
    ("6.30", "6.30"),
    ("7.30", "7.30"),
    ("8.30", "8.30"),
    ("9.30", "9.30"),
]

NO_OF_PEOPLE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
]

# RegEx on phone below implemented using Geeks for Geeks.
# Credited in readme.md


class MakeBooking(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="bookings")
    email = models.EmailField()
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(
            regex=r'^\d+$',
            message="Please enter a valid phone number.",
            code="invalid_number")]
    )
    date = models.DateField()
    time_slot = models.CharField(choices=TIME_SLOTS, max_length=5)
    number_of_people = models.IntegerField(choices=NO_OF_PEOPLE)
    special_requests = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Booking for: {self.user} on {self.date} at {self.time_slot}"
