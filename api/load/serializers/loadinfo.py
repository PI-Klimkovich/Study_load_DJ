from rest_framework import serializers

from load.models import LoadInfo


class LoadInfoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoadInfo
        fields = (
            'id',
            'academic_year',
            'faculty',
            'semester',
            'form_study',
            'discipline',
            'course_study',
            'group',
        )
