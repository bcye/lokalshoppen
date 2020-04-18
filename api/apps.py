from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        super().ready()

        import api.signals  # noqa: F401
