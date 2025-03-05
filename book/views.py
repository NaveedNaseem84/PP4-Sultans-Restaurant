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
                currentbooking.user = request.user
                currentbooking.name = request.user
                currentbooking.save()
                msg_sucessful_booking(request)
                return HttpResponseRedirect(reverse("create_booking"))
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
    msg_booking_deleted(request)
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

    booking_date = current_booking.date
    booking_time = current_booking.time_slot

    if request.method == "POST":
        form = BookingForm(request.POST, instance=current_booking)

        if form.is_valid():
            form_date = form.cleaned_data["date"]
            form_time = form.cleaned_data["time_slot"]

            if booking_info_changed(booking_date, booking_time,
                                    form_time, form_date):
                if availability_check(request, form_date, form_time):
                    form.save()
                    msg_success_booking_update(request)
                    return HttpResponseRedirect(reverse("create_booking"))

            else:
                form.save()
                msg_success_booking_update(request)
                return HttpResponseRedirect(reverse("create_booking"))

    return render(
        request,
        "book/update.html",
        {"form": form},
    )


def booking_info_changed(booking_date, booking_time, form_time, form_date):
    """
    check to see if the forms date and time are different
    from the original booking date and time.
    """
    return form_date != booking_date or form_time != booking_time


def msg_success_booking_update(request):
    """
    Sucessful update message displayed.
    """
    messages.add_message(
        request, messages.SUCCESS, "Booking successfully updated."
        )


def msg_sucessful_booking(request):
    """
    Sucessful booking message displayed.
    """
    messages.add_message(
        request, messages.SUCCESS, "booking created.")


def msg_booking_deleted(request):
    """
    Sucessful delete booking displayed
    """
    messages.add_message(
        request, messages.SUCCESS, "Booking Deleted.")
