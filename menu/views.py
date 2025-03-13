"""
Import of libraries
"""
from django.shortcuts import render
from .models import MenuItem


def menu_list(request):
    """
    creates the about us view and renders using about.html
    """
    menu = MenuItem.objects.filter(active='Yes')

    return render(
        request,
        "menu/menu.html",
        {
            "menu": menu
        },
    )
