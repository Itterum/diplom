from rest_framework import serializers

from profiles.models import Profile
from profiles.serializers import ProfileDetailSerializer

from .models import Group


class GroupsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Group
        depth = 1
        fields = "__all__"


class GroupDetailSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField()

    class Meta:
        model = Group
        depth = 1
        fields = "__all__"

    def get_students(self, obj):
        return ProfileDetailSerializer(Profile.objects.filter(group=obj,
                                       user_type='student'), many=True).data
