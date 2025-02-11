"""
Import of libraries
"""
from django.shortcuts import render
from .models import MakeBooking
from .forms import BookingForm
# Create your views here.


def create_booking(request):
    """
    creates the about us view and renders using about.html
    """
    form = BookingForm()
   
    return render(
        request,
        "book/book.html", {
            "form": form,
        },
    )
