from django.dispatch import receiver
from django.db.models.signals import post_save

from timetable.serializers import TimetableListSerializer
from .models import Department

from utils.parsing import ParseXlsx


@receiver(post_save, sender=Department)
def add_timetable(sender, instance: Department, created, **kwargs):
    update_fields = kwargs.get('update_fields')

    if created:
        if instance.basic_timetable_department.name:
            parsing(instance.basic_timetable_department)
        
        if instance.session_absentia_timetable_department.name:
            parsing(instance.session_absentia_timetable_department)

        if instance.session_timetable_department.name:
            parsing(instance.session_timetable_department)

    if update_fields is None:
        return

    if "session_timetable_department" in update_fields:
        parsing(instance.session_timetable_department)

    if "session_absentia_timetable_department" in update_fields:
        parsing(instance.session_absentia_timetable_department)

    if "basic_timetable_department" in update_fields:
        parsing(instance.basic_timetable_department)


def parsing(path: str):
    parser = ParseXlsx(path)
    data = parser.parse(to_dict=True)

    for day in data:
        serializer = TimetableListSerializer(data=day)
        serializer.is_valid(raise_exception=True)
        serializer.save()
