from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.notice import NoticeModelViewSet


router = DefaultRouter()
router.register(r"notice", NoticeModelViewSet, basename='notice')

urlpatterns = [
    path('', include(router.urls)),
]
