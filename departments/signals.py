from django.dispatch import receiver
from django.db.models.signals import post_save

from timetable.models import Timetable
from disciplines.models import Discipline
from .models import Department

from utils.parsing import ParseXlsx


@receiver(post_save, sender=Department)
def add_timetable(sender, instance: Department, created, **kwargs):
    update_fields = kwargs.get('update_fields')

    if update_fields is None and not created:
        return

    if "session_timetable_department" in update_fields:
        parsing(instance.session_timetable_department)

    if "session_absentia_timetable_department" in update_fields:
        parsing(instance.session_absentia_timetable_department)

    if "basic_timetable_department" in update_fields:
        parsing(instance.basic_timetable_department)

    raise ValueError


def parsing(path: str):
    parser = ParseXlsx(path)
    return parser.parse(to_dict=True)
