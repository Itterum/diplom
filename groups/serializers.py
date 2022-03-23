from rest_framework import serializers
from .models import Group


class GroupsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Group
        depth = 1
        fields = "__all__"


class GroupDetailSerializer(serializers.ModelField):

    students = serializers.SerializerMethodField()

    class Meta:
        model = Group
        depth = 1
        fields = "__all__"

    def get_students(self, obj):
        print(obj(obj))

        return 1