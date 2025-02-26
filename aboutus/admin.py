from django.contrib import admin
from .models import AboutUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutUs)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin page setup for the about us page.
    """
    list_display = ('title', 'description', 'added_on', 'is_valid')
    search_fields = ['title']
    summernote_fields = ('description',)
