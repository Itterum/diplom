from rest_framework import serializers
from .models import Discipline


class DisciplinesSerializer(serializers.ModelSerializer):
    """Вывод дисциплин"""

    class Meta:
        model = Discipline
        depth = 1
        fields = ('id', 'name', 'department', 'is_active')


class DisciplinesUpdateSerializer(serializers.ModelSerializer):
    """Вывод дисциплин"""

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'department', 'is_active')
