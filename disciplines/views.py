from rest_framework import viewsets
from .models import Discipline
from .serializers import DisciplinesSerializer


class DisciplinesViewSet(viewsets.ModelViewSet):
    """Листинг дисциплин"""
    serializer_class = DisciplinesSerializer
    queryset = Discipline.objects.all()
