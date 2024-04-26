from rest_framework import serializers

from load.models import Load


class LoadModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Load
        fields = (
            'id',
            'on_date',
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
