from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views, api

urlpatterns = format_suffix_patterns([
    path('students/', views.StudentViewSet.as_view({'get': 'list'})),
    path('students/<pk>/', views.StudentViewSet.as_view({'get': 'retrieve'})),

    path("departments/", views.DepartmentViewSet.as_view({'get': 'list'})),
    path("departments/<pk>/", views.DepartmentViewSet.as_view({'get': 'retrieve'})),

    path("teachers/", views.TeacherViewSet.as_view({'get': 'list'})),
    path("teachers/<pk>/", views.TeacherViewSet.as_view({'get': 'retrieve'})),

    path("groups/", views.GroupViewSet.as_view({'get': 'list'})),
    path("groups/<pk>/", views.GroupViewSet.as_view({'get': 'retrieve'})),
])
