"""
Import of libraries
"""
from django.shortcuts import render
# Create your views here.


def about_us(request):
    """
    creates the about us view and renders using about.html
    """
    return render(
        request,
        "aboutus/about.html", {
        },
    )
