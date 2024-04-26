from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.load import LoadModelViewSet


router = DefaultRouter()
router.register(r"load", LoadModelViewSet, basename='load')

urlpatterns = [
    path('', include(router.urls)),
]
