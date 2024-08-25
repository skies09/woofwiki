from rest_framework import serializers
from dogs.models import Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['group', 'breed', 'size']  # Explicitly list the fields you want to include
