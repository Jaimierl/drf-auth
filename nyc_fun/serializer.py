from rest_framework import serializers
from .models import ToDo


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'thing_to_do', 'task_description', 'created_at', 'updated_at')
        model = ToDo
    # Remember - ThingSerializer here NEEDS to remain with the name thing- it is a property of the Serializer import