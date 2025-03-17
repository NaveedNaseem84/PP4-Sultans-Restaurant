from django.urls import path
from .views import BookingManagement

# URL's structure to delete/update adapted from CI content -credited.
urlpatterns = [
    path('', BookingManagement.create_booking, name='create_booking'),

    path('delete_booking/<int:booking_id>/',
         BookingManagement.delete_booking, name='delete_booking'),

    path('update_booking/<int:booking_id>/',
         BookingManagement.update_booking, name='update_booking'),

]
