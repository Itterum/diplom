from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TimetableViewSet


router = DefaultRouter()
router.register('', TimetableViewSet, 'timetable-view')

urlpatterns = [
    path('', include(router.urls))
]
