from rest_framework import serializers
from .models import Task, HistoryTask
from django.contrib.auth import get_user_model


User = get_user_model()


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class HistoryTaskSerialiser(serializers.ModelSerializer):

    class Meta:
        model = HistoryTask
        fields = ('title',
                  'description',
                  'status',
                  'planned_completion_date')


class TaskSerialiser(serializers.ModelSerializer):
    history_task = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id',
                  'title',
                  'description',
                  'time_created',
                  'status',
                  'planned_completion_date',
                  'history_task')

    def get_history_task(self, obj):
        return HistoryTaskSerialiser(HistoryTask.objects.filter(history_task=obj), many=True, read_only=True).data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.planned_completion_date = validated_data.get('planned_completion_date', instance.planned_completion_date)

        instance.save()

        HistoryTask.objects.create(title=instance.title,
                                   description=instance.description,
                                   status=instance.status,
                                   planned_completion_date=instance.planned_completion_date,
                                   history_task=instance).save()
        return instance
