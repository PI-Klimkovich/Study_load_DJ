from rest_framework import serializers

from load.models import Discipline


class DisciplineModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = (
            'id',
            'name',
        )
