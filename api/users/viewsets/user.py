from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from api.distribution.serializers.distribution import DistributionModelSerializer
from api.notice.serializers.notice import NoticeModelSerializer
from api.users.serializers.title import TitlesModelSerializer
from api.users.serializers.user import UserModelSerializer
from user.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset

    @action(methods=['get'], detail=True, url_path='titles')
    def titles(self, request, *args, **kwargs):
        user_instance = self.get_object()
        titles_queryset = user_instance.titles_set

        serializer = TitlesModelSerializer(titles_queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='notice')
    def notice(self, request, *args, **kwargs):
        user_instance = self.get_object()
        notice_queryset = user_instance.notice_set

        serializer = NoticeModelSerializer(notice_queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='distribution')
    def load(self, request, *args, **kwargs):
        user_instance = self.get_object()
        distribution_queryset = user_instance.distribution_set

        serializer = DistributionModelSerializer(distribution_queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
