from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    name = 'departments'

    def ready(self) -> None:
        import departments.signals