from rest_framework import serializers
from .models import Discipline


class DisciplinesListSerializer(serializers.ModelSerializer):
    """Вывод дисциплин"""

    class Meta:
        model = Discipline
        depth = 1
        fields = "__all__"
