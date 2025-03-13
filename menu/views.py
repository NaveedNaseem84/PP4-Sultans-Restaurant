"""
Import of libraries
"""
from django.shortcuts import render
from .models import MenuItem


def menu_list(request):
    """
    Renders the latest menu.
    Displays individual instance of :model: `menu.MenuItem`
    **Context**
    ``menu``
        The latest instance of :model:`menu.MenuItem`
    **Template:**
    :template:`menu/menu.html`
    """
    menu = MenuItem.objects.filter(active='Yes')

    return render(
        request,
        "menu/menu.html",
        {
            "menu": menu
        },
    )
