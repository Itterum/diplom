from django.urls import path


from .views import ProfileRetrieveAPIView, ProfileUpdateAPIView


urlpatterns = [
    path('profile', ProfileRetrieveAPIView.as_view()),
    path('profile/update', ProfileUpdateAPIView.as_view()),
]
