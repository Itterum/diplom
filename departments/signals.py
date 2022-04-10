from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save

from timetable.models import Timetable
from timetable.serializers import TimetableSerializer

from .models import Department

from utils.parsing import ParseXlsx


@receiver(post_save, sender=Department)
def add_timetable(sender, instance: Department, created, **kwargs):
    update_fields = kwargs.get('update_fields')

    if created:
        if field := instance.basic_timetable_department.name:
            delete_old_schedule(field)
            parsing(field.basic_timetable_department.name)

        if field := instance.session_absentia_timetable_department.name:
            delete_old_schedule(field)
            parsing(field.session_absentia_timetable_department.name)

        if field := instance.session_timetable_department.name:
            delete_old_schedule(field)
            parsing(field.session_timetable_department.name)

    if update_fields is None:
        return

    if "session_timetable_department" in update_fields \
            and instance.session_timetable_department.name != "":
        delete_old_schedule(instance)
        parsing(instance.session_timetable_department)

    if "session_absentia_timetable_department" in update_fields \
            and instance.session_absentia_timetable_department.name != "":
        delete_old_schedule(instance)
        parsing(instance.session_absentia_timetable_department)

    if "basic_timetable_department" in update_fields \
            and instance.basic_timetable_department.name != "":
        delete_old_schedule(instance)
        parsing(instance.basic_timetable_department)


def delete_old_schedule(instance):
    Timetable.objects.filter(department=instance).delete()


@transaction.atomic
def parsing(path: str):
    parser = ParseXlsx(path)
    data = parser.parse(to_dict=True)

    for day in data:
        serializer = TimetableSerializer(data=day)
        serializer.is_valid(raise_exception=True)
        serializer.save()
