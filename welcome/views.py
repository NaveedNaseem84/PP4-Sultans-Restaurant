"""
Import of libraries
"""

from django.shortcuts import render
from .models import WelcomePromotion


def welcome_page(request):
    """
    creates the about us view and renders using about.html
    """
    promotions = WelcomePromotion.objects.filter(is_valid="Yes")
    promotions_count = promotions.count()
    return render(
        request,
        "welcome/index.html",
        {
            "promotions": promotions,
            "promotions_count": promotions_count,
        },
    )
