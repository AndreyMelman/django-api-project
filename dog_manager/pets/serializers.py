from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Breed.

    Fields:
        id (int): ID породы
        name (str): Название породы
        size (str): Размер собаки
        friendliness (int): Дружелюбие собаки
        trainability (int): Обучаемость собаки
        shedding_amount (int): Количество линьки
        exercise_needs (int): Потребность в физической активности
        dogs_count (int): Количество собак данной породы
    """

    dogs_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"


class DogListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Dog.

    Fields:
        id (int): ID собаки
        name (str): Имя собаки
        age (int): Возраст собаки
    """

    avg_breed_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Dog.

    Fields:
        id (int): ID собаки
        name (str): Имя собаки
        age (int): Возраст собаки
    """

    same_breed_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = "__all__"
