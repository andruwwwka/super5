from rest_framework import serializers

from .models import Training, TrainingSet, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'description',
            'title',
            'synchronous_vimeo_video_link',
            'tutorial_vimeo_video_link',
        ]


class TrainingSetSerializer(serializers.HyperlinkedModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingSet
        fields = ['exercises']


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    sets = TrainingSetSerializer(read_only=True, source='trainingset_set', many=True)

    class Meta:
        model = Training
        fields = ['date', 'sets']
