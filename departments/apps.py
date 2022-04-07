from django.apps import AppConfig
from django.core.signals import request_finished


class DepartmentsConfig(AppConfig):
    name = 'departments'

    def ready(self) -> None:
        from . import signals

        request_finished.connect(signals.add_timetable, signals.parsing)
