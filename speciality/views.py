from rest_framework import viewsets

from management.permissions import IsManagerOrReadOnly

from .models import Speciality
from .serializers import SpecialitySerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    """Листинг специальностей"""
    serializer_class = SpecialitySerializer
    queryset = Speciality.objects.filter(is_active=True)

    filter_fields = ['department']

    permission_classes = [IsManagerOrReadOnly]
