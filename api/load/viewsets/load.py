from rest_framework.viewsets import ModelViewSet

from api.load.serializers.load import LoadModelSerializer
from load.models import Load


class LoadModelViewSet(ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadModelSerializer
