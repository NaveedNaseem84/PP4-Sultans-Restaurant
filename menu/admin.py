"""
Import library and the MenuItem model
"""
from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin panel setup for the Menu allow.
    """
    list_display = ('name', 'description', 'price', 'category', 'active')
    search_fields = ['name', 'category', 'active']
    list_filter = ('name', 'category', 'active')
