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
        exclude = ["name"]
        fields = (
            "name",
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

    def validate_phone(self):
        """
        validation of the phone field to ensure
        there are digits only present. If not,
        raise a validation error and pass to the django
        messaging framework.

        """
        phone = self.cleaned_data("phone")
        if not phone.isdigit():
            raise forms.ValidationError("")
        return phone
