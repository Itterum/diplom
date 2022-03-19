from rest_framework import viewsets
from .models import Timetable
from .serializers import TimetableListSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    """Листинг специальностей"""
    serializer_class = TimetableListSerializer
    queryset = Timetable.objects.all()
