from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Department
import pandas as pd
from timetable.models import Timetable
from disciplines.models import Discipline
from groups.models import Group
from profiles.models import Profile
from departments.models import Department


def pars_xlsx_file(file):

    data = pd.read_excel(file)
    res = data.to_string(header=False,
                                         index=False,
                                         index_names=False).split('\n')
    obj = {
        'group_id': '',
        'days': []
    }

    template_day = {
        "day": "",
        "name": "",
        "teacher": "",
        "discipline": "",
        "department": "",
        "group": "",
        "type": "",
        "visit": "",
    }
    day = template_day

    for i in res:
        header = i.split(':')
        type_obj = header[0].strip()
        value = header[1].strip()

        if type_obj == 'group':
            obj['group_id'] = value

        if type_obj in day:
            day[type_obj] = value

        if type_obj == 'visit':
            day['visit'] = value
            day_copy = day.copy()
            obj["days"].append(day_copy)

    return obj


@receiver(post_save, sender=Department)
def my_callback(sender, instance: Department, **kwargs):
    fh = open(instance.timetable_department.path, mode='rb')
    test = pars_xlsx_file(fh)
    print(test.get('days'))


    for el in test['days']:
        print(el)
        Timetable.objects.create(
            date = el.get('day'),
            para = el.get('name'),
            visit = el.get('visit'),
            type = el.get('type'),
            discipline = Discipline.objects.get(id=el.get('name')),
            teacher = Profile.objects.get(id=el.get('teacher')),
            department = Department.objects.get(id=instance.id),
            group = Group.objects.get(code=test.get('group_id')),
        )

    print("Request finished!")
