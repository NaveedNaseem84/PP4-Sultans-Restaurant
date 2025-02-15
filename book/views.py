from datetime import date
from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MakeBooking
from .forms import BookingForm


def create_booking(request):
    """
    Creates a new booking.
    Checks availability using time slot and date
     - display a message if not availablr
    Checks to ensure the date selected is today onwards
     - display a message if its not the case
    If all the above satisfied, save booking
    """

    bookings = MakeBooking.objects.all()
    booking_count = bookings.filter(name=request.user).count()

    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form_date = form.cleaned_data["date"]
            form_time_slot = form.cleaned_data["time_slot"]

            if MakeBooking.objects.filter(
                date=form_date, time_slot=form_time_slot
            ).exists():
                messages.add_message(
                    request, messages.ERROR, "Time/Date not available."
                )
            elif form_date < date.today():
                messages.add_message(
                    request, messages.ERROR, "You can only book from today onwards!"
                )
            else:
                currentbooking = form.save(commit=False)
                currentbooking.user_id = request.user.id
                currentbooking.name = request.user
                form.save()
                messages.add_message(request, messages.SUCCESS, "Booking created.")
        return HttpResponseRedirect(reverse("create_booking"))

    form = BookingForm()

    return render(
        request,
        "book/book.html",
        {"form": form, "bookings": bookings, "booking_count": booking_count},
    )
