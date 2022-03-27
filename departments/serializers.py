from rest_framework import serializers

from .models import Department

from profiles.serializers import ProfileDetailSerializer

from news.models import News
from news.serializers import NewsListSerializer

from groups.models import Group

from gallery.serializers import GallerySerializer


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод кафедры"""

    news = serializers.SerializerMethodField()

    count_news = serializers.IntegerField(source='news_set.count')
    count_specialty = serializers.IntegerField(
        source='speciality_set.count'
    )
    count_discipline = serializers.IntegerField(source='discipline_set.count')
    count_students = serializers.IntegerField(source='profile_set.count')

    count_groups = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    gallery = GallerySerializer()

    class Meta:
        model = Department
        depth = 1
        fields = ('id', 'news', 'name', 'email', 'phone_number', 'address',
                  'description', 'photo', 'photos', 'manager_department',
                  'teachers',
                  'count_news', 'count_specialty', 'count_groups',
                  'count_discipline', 'count_students', 'gallery')

    def get_news(self, obj):
        return NewsListSerializer(News.objects.filter(department=obj),
                                  many=True).data

    def get_count_groups(self, obj):
        speciality = obj.speciality_set.all()
        groups = Group.objects.filter(spec__in=speciality).count()
        return groups

    def get_teachers(self, obj):
        return ProfileDetailSerializer(
            obj.profile_set.filter(user_type="teacher"), many=True).data
