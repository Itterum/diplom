from rest_framework import viewsets
from .models import Speciality
from .serializers import SpecialityListSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    """Листинг специальностей"""
    serializer_class = SpecialityListSerializer
    queryset = Speciality.objects.all()

    filter_fields = ['department']
