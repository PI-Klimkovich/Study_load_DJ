from rest_framework import serializers

from load.models import OnDate


class OnDateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnDate
        fields = (
            'id',
            'on_date',
            'note',
        )
