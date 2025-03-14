"""
Import of libraries
"""

from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    """
    Renders the latest about us content
    Displays individual instance of :model: `aboutus.AboutUs`

    **Context**
        ``aboutus``
            The latest instance of :model:`aboutus.AboutUs`
    **Template:**
        :template:`aboutus/about.html`
    """
    aboutus = AboutUs.objects.filter(is_valid="Yes").first()
    return render(
        request,
        "aboutus/about.html",
        {
            "aboutus": aboutus,
        },
    )
