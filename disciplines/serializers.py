from rest_framework import serializers
from .models import Discipline


class DisciplinesListSerializer(serializers.ModelSerializer):
    """Вывод дисциплин"""

    class Meta:
        model = Discipline
        fields = "__all__"
