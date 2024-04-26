from rest_framework import serializers

from load.models import Group


class GroupModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
        )
