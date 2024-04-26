from rest_framework.viewsets import ModelViewSet

from api.distribution.serializers.distribution import DistributionModelSerializer
from distribution.models import Distribution


class DistributionModelViewSet(ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionModelSerializer
