from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    #auth
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),

]
