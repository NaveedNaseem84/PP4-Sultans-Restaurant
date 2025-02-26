"""
Import of libraries
"""

from django.shortcuts import render
from .models import AboutUs
# Create your views here.


def about_us(request):
    """
    creates the about us view and renders using about.html
    """
    #about = AboutUs.objects.all()
    aboutus = AboutUs.objects.filter(is_valid="Yes")
    return render(
        request,
        "aboutus/about.html",
        {
            "aboutus": aboutus,
        },
    )
