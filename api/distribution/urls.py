from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.distribution import DistributionModelViewSet


router = DefaultRouter()
router.register(r"distribution", DistributionModelViewSet, basename='distribution')

urlpatterns = [
    path('', include(router.urls)),
]
