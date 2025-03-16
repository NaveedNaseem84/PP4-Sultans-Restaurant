"""
Import of Django libraries, model and form
"""

from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date
from .models import MakeBooking
from .forms import BookingForm


class BookingManagement():

    def availability_check(request, form_date, form_time_slot):
        """
        Availability check of a booking on a requested date/time
        against records in : :model:`book.MakeBooking`.

        Checks performed:
        - The date is not in the past
        - The date/time requested is available to book
        - Display relevant message if not satisfied.

         **Context**
            ``form_date``
                requested date from form
            ``form_time_slot``
                requested time from form
        """
        if MakeBooking.objects.filter(date=form_date,
                                      time_slot=form_time_slot).exists():
            BookingManagement.msg_date_time_unavailable(request)
            return False
        elif form_date < date.today():
            BookingManagement.msg_no_backward_date(request)
            return False
        return True

    @login_required
    def create_booking(request):
        """
        Creates a new booking for the authenticated user.

        - Checks availability for the timeslot on the given day.
        - Checks to ensure the date selected is today onwards.
        - Displays relevant message if conditions not met.

        If all the above satisfied, booking is created with details
        provided along with a success message.

        **Context**
            ``bookings``
                Bookings for the current user from the
                instance :model:`book.MakeBooking`
            ``booking_count``
                Total number of bookings for current user.
            ``form``
                An instance of :form:`book.BookingForm`
        **Decorator**
            ``@login_required``
                user login required for this view.
        **Template**
            :template:`book/book.html`
        """

        if request.method == "POST":
            form = BookingForm(data=request.POST)

            if form.is_valid():
                form_date = form.cleaned_data["date"]
                form_time_slot = form.cleaned_data["time_slot"]
                availability_check = BookingManagement.availability_check(
                    request, form_date,
                    form_time_slot)

                if availability_check:
                    currentbooking = form.save(commit=False)
                    currentbooking.user = request.user
                    currentbooking.save()
                    BookingManagement.msg_sucessful_booking(request)
                    return HttpResponseRedirect(reverse("create_booking"))
        else:
            form = BookingForm()

        bookings = MakeBooking.objects.filter(user=request.user)
        booking_count = bookings.count()

        return render(
            request,
            "book/book.html",
            {"form": form,
             "bookings": bookings,
             "booking_count": booking_count},
        )
    # Structure to delete - adapted from CI content
    # Credited in readme.md

    @login_required
    def delete_booking(request, booking_id):
        """
        Delete the selecting booking after confirmation.
        Message displayed to confirm delete.

        **Context**
            ``booking``
                A selected instance of :model:`book.MakeBooking`
         **Decorator**

            ``@login_required``
                user login required for this view.
        """
        booking = get_object_or_404(MakeBooking, id=booking_id)
        booking.delete()
        BookingManagement.msg_booking_deleted(request)
        return HttpResponseRedirect(reverse("create_booking"))

    # Structure to update - adapted from CI content
    # Credited in readme.md

    @login_required
    def update_booking(request, booking_id):
        """
        Update the selected booking for authenticated user.

        - Checks to see if the time/date has changed from booking.
        - Checks availability for the timeslot on the given day.
        - Checks to ensure the date selected is today onwards.
        - Displays relevant message if conditions not met.

        If all the above satisfied, booking is updated with details
        provided along with a success message.

         **Context**
            ``current_booking``
                A selected instance of :model:`book.MakeBooking`
            ``booking_date``
                Current date on booking
            ``booking_time``
                Current time on booking
            ``form``
                Current booking via instance of :form:`book.BookingForm`

         **Decorator**
            ``@login_required``
                user login required for this view.

         **Template**
            :template:`book/update.html`
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

                booking_info_changed = BookingManagement.booking_info_changed(
                    booking_date, booking_time, form_time, form_date
                )

                if booking_info_changed:
                    availability_check = BookingManagement.availability_check(
                        request,
                        form_date, form_time)

                    if availability_check:
                        form.save()
                        BookingManagement.msg_update_sucess(request)
                        return HttpResponseRedirect(reverse("create_booking"))

                    else:
                        return render(request, "book/update.html",
                                      {"form": form})

                else:
                    form.save()
                    BookingManagement.msg_update_sucess(request)
                    return HttpResponseRedirect(reverse("create_booking"))

        return render(request, "book/update.html", {"form": form})

    def booking_info_changed(booking_date, booking_time, form_time, form_date):
        """
        Used within ``updated_booking``- Check to see if the forms date
        and time are different from the original booking date and time.

         **Context**
            ``booking_date``
                Current booking date
            ``booking_time``
                Current booking time
            ``form_date``
                Requested date
            ``form_time``
                Requested time
        """
        return form_date != booking_date or form_time != booking_time

    # messages functions

    def msg_update_sucess(request):
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

    def msg_date_time_unavailable(request):
        """
        Time slot on date not available displayed.
        """
        messages.add_message(
            request, messages.ERROR,
            "Sorry, time slot unavailable on this date.")

    def msg_no_backward_date(request):
        """
        Time slot on date not available displayed.
        """
        messages.add_message(
            request, messages.ERROR,
            "You can only book from today onwards!")
