from django.contrib import admin
from .models import AboutUs

@admin.register(AboutUs)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin page setup for the about us page.
    """
    list_display = ('title', 'description', 'added_on', 'is_valid')
    search_fields = ['title']
