from rest_framework import serializers
from .models import Group


class GroupsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Group
        fields = "__all__"
