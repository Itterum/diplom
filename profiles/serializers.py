from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from mixins.serializers import Base64ImageField

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        depth = 1
        fields = (
            'id', 'username', 'department', 'full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number', 'user_type',
            'address', 'photo', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'department': {'read_only': True},
            'full_name': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'gender': {'read_only': True},
            'birth_date': {'read_only': True},
            'user_type': {'read_only': True},
            'group': {'read_only': True},
        }


class ProfileUpdateSerializer(serializers.ModelSerializer):

    photo = Base64ImageField(allow_null=True)

    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'department', 'full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number', 'user_type',
            'address', 'photo', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification',
        )


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        depth = 1
        fields = ('id', 'full_name', 'photo', 'gender')


class ProfileCreateSerializer(UserCreateSerializer):

    photo = Base64ImageField(allow_null=True)

    class Meta:
        model = UserCreateSerializer.Meta.model
        fields = UserCreateSerializer.Meta.fields + (
            'username',
            'department', 'full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number', 'user_type',
            'address', 'photo', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification',
        )


class ProfileValidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('email',)
