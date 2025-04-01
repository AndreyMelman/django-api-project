from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    dogs_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"


class DogListSerializer(serializers.ModelSerializer):
    avg_breed_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(serializers.ModelSerializer):
    same_breed_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = "__all__"
