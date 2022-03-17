from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from . import views

# router = DefaultRouter()
# router.register('profiles', views.ProfileViewSet)

urlpatterns = [
    #auth
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),

    # path('users/', views.UserViewSet.as_view({'get': 'list'})),
    # path('profiles/', views.ProfileViewSet.as_view({'get': 'list'})),
    # path('profiles/<pk>/', views.ProfileViewSet.as_view({'get': 'retrieve'})),
    # path('profiles/', )
    # path('students/', views.StudentViewSet.as_view({'get': 'list'})),
    # path('students/<pk>/', views.StudentViewSet.as_view({'get': 'retrieve'}))
]
