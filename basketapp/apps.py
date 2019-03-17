from django.apps import AppConfig


class BasketappConfig(AppConfig):
    name = 'basketapp'

    def ready(self):
        import basketapp.signals
