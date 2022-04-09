from rest_framework import serializers

from profiles.models import Profile
from profiles.serializers import ProfileDetailSerializer

from .models import Group


class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        depth = 1
        fields = ('id', 'code', 'email', 'phone_number', 'spec',
                  'headmen', 'curator', 'visit_type', 'start_date', 'is_session')


class GroupDetailSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField()

    class Meta:
        model = Group
        depth = 1
        fields = ('id', 'code', 'email', 'phone_number', 'spec',
                  'headmen', 'curator', 'visit_type', 'start_date', 'is_session',
                  'students')

    def get_students(self, obj):
        return ProfileDetailSerializer(Profile.objects.filter(group=obj,
                                       user_type='student'), many=True).data
