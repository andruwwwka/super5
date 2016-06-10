from rest_framework import serializers
from accounts.serializations import UserSerializer
from .models import Athlete, TargetPriority, Target, ZonePriority, Zone


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['slug']


class TargetPrioritySerializer(serializers.ModelSerializer):
    target_priority = TargetSerializer()

    class Meta:
        model = TargetPriority
        fields = ['priority', 'target_priority']


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['slug']


class ZonePrioritySerializer(serializers.ModelSerializer):
    zone_priority = ZoneSerializer(many=False, read_only=True)

    class Meta:
        model = ZonePriority
        fields = ['priority', 'zone_priority']


class AthleteSerializer(serializers.ModelSerializer):
    # При необходимости отображать приоритеты и зоны, только разремарить
    # targetpriority_set = TargetPrioritySerializer(many=True)
    # zonepriority_set = ZonePrioritySerializer(many=True)

    class Meta:
        model = Athlete
        fields = [
            'height', 'width', 'gender', 'training_duration',
            'birthday', 'confirmed', 'level', 'week_day',
            'actual_date'
            # 'targetpriority_set', 'zonepriority_set',
        ]


class AthleteAllDataSerializer(serializers.ModelSerializer):
    targetpriority_set = TargetPrioritySerializer(many=True, read_only=True)
    zonepriority_set = ZonePrioritySerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Athlete
        fields = [
            'height',
            'width',
            'gender',
            'training_duration',
            'birthday',
            'confirmed',
            'level',
            'week_day',
            'user',
            'targetpriority_set',
            'zonepriority_set',
            'actual_date',
            'exercise_length_in_seconds',
            'chill_length_in_seconds'
        ]
