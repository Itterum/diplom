from rest_framework import serializers
from .models import Discipline


class DisciplinesListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Discipline
        fields = "__all__"
