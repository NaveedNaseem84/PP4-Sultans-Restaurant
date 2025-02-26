"""
Import of libraries, model and form
"""

from datetime import date
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MakeBooking
from .forms import BookingForm


def availability_check(request, form_date, form_time_slot):
    """
    Validation of the booking.
    """
    if MakeBooking.objects.filter(date=form_date,
                                  time_slot=form_time_slot).exists():
        messages.add_message(
            request, messages.ERROR,
            "Sorry, time slot unavailable on this date."
        )
        return False
    elif form_date < date.today():
        messages.add_message(
            request, messages.ERROR, "You can only book from today onwards!"
        )
        return False
    return True


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

            if availability_check(request, form_date, form_time_slot):
                currentbooking = form.save(commit=False)
                currentbooking.user_id = request.user.id
                currentbooking.name = request.user
                currentbooking.save()
                messages.add_message(request, messages.SUCCESS,
                                     "booking created.")
                return HttpResponseRedirect(reverse("create_booking"))

        else:
            messages.add_message(
                request, messages.ERROR,
                "Please enter a valid phone number."
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
    messages.add_message(request, messages.SUCCESS, "Booking Deleted.")
    return HttpResponseRedirect(reverse("create_booking"))


def update_booking(request, booking_id):
    """
    update the selected booking. Selected booking values
    are passed to the form ready for the update.
    Form again is validated and checked against availability.
    If successfully, updated, if not message displayed.
    """

    current_booking = get_object_or_404(MakeBooking, id=booking_id)
    form = BookingForm(instance=current_booking)

    current_booking_date = current_booking.date
    current_booking_time = current_booking.time_slot

    if request.method == "POST":
        form = BookingForm(request.POST, instance=current_booking)

        if form.is_valid():
            form_date = form.cleaned_data["date"]
            form_time_slot = form.cleaned_data["time_slot"]

            if (
                form_date != current_booking_date
                or form_time_slot != current_booking_time
            ):
                if availability_check(request, form_date, form_time_slot):
                    form.save()

                    messages.add_message(
                        request, messages.SUCCESS,
                        "Booking successfully updated."
                    )
                    return HttpResponseRedirect(reverse("create_booking"))

            else:
                form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Booking successfully updated."
                )
                return HttpResponseRedirect(reverse("create_booking"))

    return render(
        request,
        "book/update.html",
        {"form": form},
    )
