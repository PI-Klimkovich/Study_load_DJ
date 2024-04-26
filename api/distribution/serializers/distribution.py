from rest_framework import serializers

from distribution.models import Distribution


class DistributionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distribution
        fields = (
            'id',
            'load',
            'lectures',
            'laboratory',
            'practical',
            'course_work',
            'calculation_and_graphic_works',
            'control',
            'consultations',
            'tests',
            'exams',
            'diploma',
            'state_exam',
            'practice',
            'postgraduate_studies',
            'total',
            'note',
        )
