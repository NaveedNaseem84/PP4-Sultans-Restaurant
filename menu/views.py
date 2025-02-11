"""
Import of libraries
"""
from django.shortcuts import render
# Create your views here.


def menu_list(request):
    """
    creates the about us view and renders using about.html
    """

    return render(
        request,
        "menu/menu.html", {
        },
    )
