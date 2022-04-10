from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token
from ajax_select import urls as ajax_select_urls

from .yasg import urlpatterns as doc_urls

from .routers import (
    newsRouter,
    departmentsRouter,
    specialityRouter,
    disciplinesRouter,
    groupsRouter,
    galleryRouter,
    peoplesRouter
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
    path('ajax_select/', include(ajax_select_urls)),

    # authorization
    path('api/v1/', include("djoser.urls.base")),
    path('api/v1/auth/token-create/', obtain_jwt_token, name='obtain_jwt_token'),

    path('api/v1/profiles/', include('profiles.urls')),
    path('api/v1/timetable/', include('timetable.urls')),
    path('api/v1/management/', include('management.urls')),

    path('api/v1/news/', include(newsRouter.urls)),
    path('api/v1/groups/', include(groupsRouter.urls)),
    path('api/v1/departments/', include(departmentsRouter.urls)),
    path('api/v1/speciality/', include(specialityRouter.urls)),
    path('api/v1/disciplines/', include(disciplinesRouter.urls)),
    path('api/v1/gallery/', include(galleryRouter.urls)),
    path('api/v1/peoples/', include(peoplesRouter.urls)),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
