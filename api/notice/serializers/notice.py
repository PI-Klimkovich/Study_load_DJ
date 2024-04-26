from rest_framework import serializers

from notice.models import Notice


class NoticeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = (
            'uuid',
            'message',
            'created_at',
            'mod_time',
            'user',
        )
