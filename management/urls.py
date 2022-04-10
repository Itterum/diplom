from django.urls import path

from .views import AuthManager


urlpatterns = [
    path('auth/', AuthManager.as_view())
]
