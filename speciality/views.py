from rest_framework import viewsets
from .models import Speciality
from .serializers import SpecialityListSerializer


# Create your views here.
class SpecialityViewSet(viewsets.ModelViewSet):
    """Листинг специальностей"""
    serializer_class = SpecialityListSerializer
    queryset = Speciality.objects.all()
