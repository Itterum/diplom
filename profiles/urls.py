from django.urls import path


from .views import ProfileRetrieveAPIView, ProfileUpdateAPIView


urlpatterns = [
    path('profile', ProfileUpdateAPIView.as_view()),
    path('profile/update', ProfileRetrieveAPIView.as_view()),
]
