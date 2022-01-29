from profiles.views import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ProfileViewSet)
# router.register('', StudentViewSet)