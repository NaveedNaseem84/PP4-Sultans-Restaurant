"""
import of libraries
"""
from django.contrib import admin
from .models import WelcomePromotion

@admin.register(WelcomePromotion)
class PromotionsAdmin(admin.ModelAdmin):
    """
    Admin page setup for the promotions.
    """

    list_display = ('promotion_title', 'is_valid')
    search_fields = ['promotion_title', 'description']
