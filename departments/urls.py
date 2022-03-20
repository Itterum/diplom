from django.urls import path

from .views import DepartmentsViewSet


urlpatterns = [
    path('', DepartmentsViewSet.as_view({'get': 'list'})),
    path('<int:pk>', DepartmentsViewSet.as_view({'get': 'retrieve'})),
]
