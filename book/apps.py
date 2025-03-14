from django.apps import AppConfig


class BookConfig(AppConfig):
    """
    Book app configuration

    **context**
        ``default_auto_field``
            django.db.models.BigAutoField
        ``name``
            book
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
