from rest_framework.viewsets import ModelViewSet

from api.users.serializers.user import UserModelSerializer
from user.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
