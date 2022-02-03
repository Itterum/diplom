from profiles.views import ProfileViewSet
from departments.views import DepartmentsViewSet
from news.views import NewsViewSet
from rest_framework import routers

profilesRouter = routers.DefaultRouter()
profilesRouter.register('', ProfileViewSet)

departmentsRouter = routers.DefaultRouter()
departmentsRouter.register('', DepartmentsViewSet)

newsRouter = routers.DefaultRouter()
newsRouter.register('', NewsViewSet)
