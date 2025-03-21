from django.apps import AppConfig


class WelcomeConfig(AppConfig):
    """
    welcome app configuration

    **context**
        ``default_auto_field``
            django.db.models.BigAutoField
        ``name``
            welcome
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'welcome'
