from rest_framework import serializers
from .models import Group


class GroupsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Group
        depth = 1
        fields = "__all__"
