from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class UserModelSerializer(serializers.ModelSerializer):
    # middle_name = serializers.CharField(required=True)  # переопределение поля на обязательное
    # phone = serializers.CharField(required=True)  # переопределение поля на обязательное
    # email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())], required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'phone',
            'address',
            'email',
            'photo',
            'description',
            'is_member',
        )

    # def validate_phone(self, value):
    #     # собственная валидация поля: метод должен начинаться с validate_ + поле
    #     if not value.startswith('+'):
    #         raise serializers.ValidationError('Телефон должен начинаться с "+"')
    #     return value
