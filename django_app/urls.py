"""django_app URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .routers import profilesRouter, newsRouter, departmentsRouter, specialityRouter, disciplinesRouter, groupsRouter, timetableRouter

from .yasg import urlpatterns as doc_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    # пути для авторизация
    path("api/v1/", include("djoser.urls.base")),
    path('api/v1/auth/', include('profiles.urls')),

    path('api/v1/profiles/', include(profilesRouter.urls)),
    path('api/v1/news/', include(newsRouter.urls)),
    path('api/v1/departments/', include(departmentsRouter.urls)),
    path('api/v1/speciality/', include(specialityRouter.urls)),
    path('api/v1/disciplines/', include(disciplinesRouter.urls)),
    path('api/v1/groups/', include(groupsRouter.urls)),
    path('api/v1/timetable/', include(timetableRouter.urls)),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
