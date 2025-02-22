from django.contrib import admin
from .models import MakeBooking


@admin.register(MakeBooking)
class BookAdmin(admin.ModelAdmin):
    """
    Admin panel structure for the bookings.
    """

    list_display = ("name", "date", "time_slot", "number_of_people")
