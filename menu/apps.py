"""
Import of libraries
"""
from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Menu app configuration

    **context**
        ``default_auto_field``
            django.db.models.BigAutoField
        ``name``
            menu
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
