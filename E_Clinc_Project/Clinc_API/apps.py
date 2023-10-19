from django.apps import AppConfig


class ClincApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Clinc_API'
    model = 'Clinc_API.models'

