from datetime import date
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MakeBooking
from .forms import BookingForm


def create_booking(request):
    """
    Creates a new booking.
    Checks availability using time slot and date
     - display a message if not available
    Checks to ensure the date selected is today onwards
     - display a message if its not the case
    If all the above satisfied, save booking
    """

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
                    request, messages.ERROR, 
                    "You can only book from today onwards!"
                )
            else:
                currentbooking = form.save(commit=False)
                currentbooking.user_id = request.user.id
                currentbooking.name = request.user
                currentbooking.save()
                messages.add_message(
                    request, messages.SUCCESS, "booking created.")
                return HttpResponseRedirect(reverse("create_booking"), form)
        else:
            messages.add_message(
                request, messages.ERROR, "Please enter a valid phone number."
            )
    else:
        form = BookingForm()

    bookings = MakeBooking.objects.filter(name=request.user)
    booking_count = bookings.count()

    return render(
        request,
        "book/book.html",
        {"form": form, "bookings": bookings, "booking_count": booking_count},
    )


def delete_booking(request, booking_id):
    """
    delete the selecting booking. A confirmation of the 
    delete will be impletemented within book.html
    """
    booking = get_object_or_404(MakeBooking, id=booking_id)
    booking.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Booking Deleted.'
    )
    return HttpResponseRedirect(reverse('create_booking'))
