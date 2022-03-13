from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# router = DefaultRouter()
# router.register('profiles', views.ProfileViewSet)

urlpatterns = format_suffix_patterns([
    #auth
    # path('token/', views.TokenObtainView.as_view(), name='new-token,obtain-view'),
    # path('departments/', views.DepartmentsViewSet.as_view(), name='departments')
    # path('users/', views.UserViewSet.as_view({'get': 'list'})),
    # path('profiles/', views.ProfileViewSet.as_view({'get': 'list'})),
    # path('profiles/<pk>/', views.ProfileViewSet.as_view({'get': 'retrieve'})),
    # path('profiles/', )
    # path('students/', views.StudentViewSet.as_view({'get': 'list'})),
    # path('students/<pk>/', views.StudentViewSet.as_view({'get': 'retrieve'}))
])
