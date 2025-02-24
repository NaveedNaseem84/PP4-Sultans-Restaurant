from django.urls import path
from . import views

urlpatterns = [   
    path('', views.create_booking, name='create_booking'),

    path('delete_booking/<int:booking_id>/',views.delete_booking, name='delete_booking'),

    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),

]
