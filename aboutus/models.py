"""
Import of libraries
"""
from django.db import models

VALID_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),
    ]


class AboutUs(models.Model):
    """
    Stores a single about us entry.
    """
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    added_on = models.DateField(auto_now_add=True)
    is_valid = models.CharField(
        choices=VALID_CHOICES, max_length=3, blank=False)

    def __str__(self):
        return f"About page: {self.title}"
