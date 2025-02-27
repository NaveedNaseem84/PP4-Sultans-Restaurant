"""
Import of libraries
"""

from django.shortcuts import render
from .models import WelcomePromotion
# Create your views here.


def welcome_page(request):
    """
    creates the about us view and renders using about.html
    """
    promotions = WelcomePromotion.objects.filter(is_valid="Yes")
    return render(
        request,
        "welcome/index.html",
        {
            "promotions": promotions,
        },
    )
