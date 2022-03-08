from rest_framework import serializers

from todos.models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
