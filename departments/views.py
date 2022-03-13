import pandas as pd
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Department
from .serializers import (
    DepartmentsListSerializer,
)


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
        "type": "",
        "visit": "",
    }
    day = template_day

    for i in res:
        header = i.split(':')
        type_obj = header[0].strip()
        value = header[1].strip()
        count = 0

        if type_obj == 'group':
            obj['group_id'] = value

        if count == 0:
            day = template_day

        if type_obj == 'day':
            count += 1
            day['day'] = value

        if type_obj == 'name':
            day['name'] = value

        if type_obj == 'teacher':
            day['teacher'] = value

        if type_obj == 'type':
            day['type'] = value

        if type_obj == 'visit':
            day['visit'] = value
            obj["days"].append(day)
            count = 0

    return obj


# Create your views here.
class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentsListSerializer
    queryset = Department.objects.all()

