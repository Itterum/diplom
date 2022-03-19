from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        depth = 1
        fields = "__all__"
