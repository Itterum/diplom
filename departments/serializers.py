from rest_framework import serializers
from .models import Department
from news.models import News
from profiles.models import Profile
from news.serializers import NewsListSerializer
from profiles.serializers import ProfileSerializer

class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    news = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ("id","name","email","phone_number","address","manager_department","description","photo","photos","news","teachers","department")

    def get_news(self,obj):
        return NewsListSerializer(News.objects.filter(department = obj),many=True).data

    def get_teachers(self,obj):
        teachers = Profile.objects.filter(user_type = 'teacher')
        return ProfileSerializer(teachers.filter(department = obj),many=True).data

