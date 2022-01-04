from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from core.skills.viewsets import FruitViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


router.register(r'fruits', FruitViewSet)


urlpatterns = router.urls