from rest_framework import routers

from departments.views import DepartmentsViewSet
from speciality.views import SpecialityViewSet
from news.views import NewsViewSet
from disciplines.views import DisciplinesViewSet
from groups.views import GroupsViewSet
from timetable.views import TimetableViewSet

from profiles.views import PeoplesViewSet

departmentsRouter = routers.DefaultRouter()
departmentsRouter.register('', DepartmentsViewSet)

newsRouter = routers.DefaultRouter()
newsRouter.register('', NewsViewSet)

specialityRouter = routers.DefaultRouter()
specialityRouter.register('', SpecialityViewSet)

disciplinesRouter = routers.DefaultRouter()
disciplinesRouter.register('', DisciplinesViewSet)

groupsRouter = routers.DefaultRouter()
groupsRouter.register('', GroupsViewSet)

timetableRouter = routers.DefaultRouter()
timetableRouter.register('', TimetableViewSet)

peoplesRouter = routers.DefaultRouter()
peoplesRouter.register('', PeoplesViewSet)
