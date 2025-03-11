from django.contrib import admin
from .models import MakeBooking


@admin.register(MakeBooking)
class BookAdmin(admin.ModelAdmin):
    """
    Admin panel structure for the bookings.
    """
    list_display = ("user", "date", "time_slot", "number_of_people")
    search_fields = ['user__username', 'email', 'date', 'phone']
    list_filter = ('date', 'time_slot')
