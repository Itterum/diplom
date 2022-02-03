from rest_framework import viewsets
from .models import Discipline
from .serializers import DisciplinesListSerializer


# Create your views here.
class DisciplinesViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = DisciplinesListSerializer
    queryset = Discipline.objects.all()
