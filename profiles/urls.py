from django.urls import path

from .views import ProfileRetrieveAPIView


urlpatterns = [
    path('profile', ProfileRetrieveAPIView.as_view()),
]
