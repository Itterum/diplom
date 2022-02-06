from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    name = 'departments'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
         import departments.signals