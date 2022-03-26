import profile
from rest_framework import serializers

from .models import Department

from profiles.models import Profile
from profiles.serializers import ProfileDetailSerializer

from news.models import News
from news.serializers import NewsSerializer

from groups.models import Group


class DepartmentsSerializer(serializers.ModelSerializer):
    """Вывод кафедры"""

    news = serializers.SerializerMethodField()

    count_news = serializers.IntegerField(source='news_set.count')
    count_specialty = serializers.IntegerField(
        source='speciality_set.count'
    )
    count_groups = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Department
        depth = 1
        fields = ('id', 'news', 'name', 'email', 'phone_number', 'address',
                  'description', 'photo', 'photos', 'manager_department',
                  'teachers',
                  'count_news', 'count_specialty', 'count_groups')

    def get_news(self, obj):
        return NewsSerializer(News.objects.filter(department=obj),
                                  many=True).data

    def get_count_groups(self, obj):
        speciality = obj.speciality_set.all()
        groups = Group.objects.filter(spec__in=speciality).count()
        return groups

    def get_teachers(self, obj):
        return ProfileDetailSerializer(
            obj.profile_set.filter(user_type="teacher"), many=True).data
