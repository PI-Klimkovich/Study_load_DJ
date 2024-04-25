from rest_framework import serializers

from user.models import Titles


class TitlesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Titles
        fields = (
            'id',
            'assignment_date',
            'job_title',
            'academic_degree',
            'academic_title',
        )
