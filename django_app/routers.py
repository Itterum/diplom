from profiles.views import ProfileViewSet
from departments.views import DepartmentsViewSet
from speciality.views import SpecialityViewSet
from news.views import NewsViewSet
from disciplines.views import DisciplinesViewSet
from rest_framework import routers

profilesRouter = routers.DefaultRouter()
profilesRouter.register('', ProfileViewSet)

departmentsRouter = routers.DefaultRouter()
departmentsRouter.register('', DepartmentsViewSet)

newsRouter = routers.DefaultRouter()
newsRouter.register('', NewsViewSet)

specialityRouter = routers.DefaultRouter()
specialityRouter.register('', SpecialityViewSet)

disciplinesRouter = routers.DefaultRouter()
disciplinesRouter.register('', DisciplinesViewSet)
