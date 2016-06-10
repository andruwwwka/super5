from rest_framework import serializers
from .models import FiveUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Напрямую использовать модель пользователя только здесь!!!
        model = FiveUser
        fields = ('email', 'is_staff')
