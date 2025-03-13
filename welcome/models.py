"""
Import of libraries
"""
from django.db import models

VALID_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),
    ]


class WelcomePromotion(models.Model):
    """
    Model structure for the promotions to be
    displayed on the home page.
    """
    promotion_title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    is_valid = models.CharField(
        choices=VALID_CHOICES,
        max_length=3, blank=False)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Promotion: {self.promotion_title}"
