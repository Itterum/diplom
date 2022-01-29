"""django_app URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .routers import router

from .yasg import urlpatterns as doc_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),

    # пути для авторизация
    path("api/v1/", include("djoser.urls.base")),
    path('api/v1/auth/', include('profiles.urls')),
    # path('api-auth/', include('profiles.urls')),
    # path("api-auth/", include("djoser.urls.authtoken")),
    # path("auth/", include("djoser.urls.jwt")),
    # path("auth/", include("djoser.social.urls")),

    # Пути моделей
    # path('api/v1/', include('university.urls')),
    path('api/v1/profiles/', include(router.urls)),
    path('api/v1/students/', include(router.urls))
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
