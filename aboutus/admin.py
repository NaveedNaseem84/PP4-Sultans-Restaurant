"""
Import of libraries
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import AboutUs


@admin.register(AboutUs)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin page setup for the about us page.

    **Context**
        ``list_display``
            title, description, added_on, is_valid
        ``search_fields``
            title
        ``summernote_fields``
            description
    """
    list_display = ('title', 'description', 'added_on', 'is_valid')
    search_fields = ['title']
    summernote_fields = ('description',)
