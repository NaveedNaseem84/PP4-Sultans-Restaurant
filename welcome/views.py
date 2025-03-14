"""
Import of libraries
"""

from django.shortcuts import render
from .models import WelcomePromotion


def welcome_page(request):
    """
    Renders the latest home page with promotions.
    Displays individual instance of :model:`welcome.WelcomePromotion`

    **Context**
        ``promotions``
            The latest instance of :model:`welcome.WelcomePromotion`
        ``promotions_count``
            A count of the promotions retrieved.
    **Template:**
        :template:`welcome/index.html`
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
