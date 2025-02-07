"""
Import of libraries
"""
from django.shortcuts import render
# Create your views here.


def create_booking(request):
    """
    creates the about us view and renders using about.html
    """
   
    return render(
        request,
        "book/book.html", {
        },
    )
