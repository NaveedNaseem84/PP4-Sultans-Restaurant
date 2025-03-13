"""
Import of libraries
"""

from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    """
    creates the about us view and renders using about.html
    """
    aboutus = AboutUs.objects.filter(is_valid="Yes").first()
    return render(
        request,
        "aboutus/about.html",
        {
            "aboutus": aboutus,
        },
    )
