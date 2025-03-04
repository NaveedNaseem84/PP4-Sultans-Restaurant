"""
Import of libraries
"""
from django.db import models

CATEGORIES_CHOICES = [
    ("Starter", "Starter"),
    ("Side", "Side"),
    ("Dessert", "Dessert"),
    ("Main", "Main"),
    ("Drink", "Drink"),
    ]

ACTIVE_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),
    ]


class MenuItem(models.Model):
    """
    Model structure for the menu.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=7, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    added_on = models.DateField(auto_now_add=True)
    active = models.CharField(choices=ACTIVE_CHOICES, max_length=3, blank=False)

    def __str___(self):
        return f"Menu item: {self.name} Active: {self.active}"
