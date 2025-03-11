"""
Import of libaries and booking model
"""

from django import forms
from .models import MakeBooking


class BookingForm(forms.ModelForm):
    """
    main class for the form
    """

    class Meta:
        """
        values to be formatted and displayed as form.
        """

        model = MakeBooking
        fields = (
            "email",
            "phone",
            "date",
            "time_slot",
            "number_of_people",
            "special_requests",
        )
        widgets = {
            "date": forms.TextInput(attrs={"type": "date"}),
            "special_requests": forms.Textarea(attrs={"rows": "3"}),
        }
