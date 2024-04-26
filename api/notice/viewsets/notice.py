from rest_framework.viewsets import ModelViewSet

from api.notice.serializers.notice import NoticeModelSerializer
from notice.models import Notice


class NoticeModelViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeModelSerializer
