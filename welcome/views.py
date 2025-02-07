"""
Import of libraries
"""
from django.shortcuts import render
# Create your views here.


def welcome_page(request):
    """
    creates the about us view and renders using about.html
    """
    return render(
        request,
        "welcome/index.html", {
        },
    )
