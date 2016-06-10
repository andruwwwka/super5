from rest_framework import serializers
from extend_notifications.models import RestNotification
from django.contrib.auth import get_user_model

from athletes.models import Athlete


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestNotification
        fields = ('id', 'body', )


class DayWeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('week_day',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        get_user_model().objects.create_user(email, password)
