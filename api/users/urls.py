from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.user import UserModelViewSet


router = DefaultRouter()
router.register(r"users", UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
