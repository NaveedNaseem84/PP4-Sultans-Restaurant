"""
Import of libraries
"""
from django.apps import AppConfig


class AboutusConfig(AppConfig):
    """
    About us app configuration

    **context**
        ``default_auto_field``
            django.db.models.BigAutoField
        ``name``
            aboutus
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aboutus'
