from django.db import models


class Dog(models.Model):
    """
    Модель собаки.

    Attributes:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (Breed): Порода собаки.
        gender (str): Пол собаки.
        color (str): Цвет собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
    """

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    favorite_food = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=50)

    def __str__(self):
        return self.name and f"({self.breed})"


class Breed(models.Model):
    """
    Модель породы собаки.

    Attributes:
        name (str): Название породы.
        size (str): Размер собаки (Tiny, Small, Medium, Large).
        friendliness (int): Дружелюбие собаки (1-5).
        trainability (int): Обучаемость собаки (1-5).
        shedding_amount (int): Количество линьки (1-5).
        exercise_needs (int): Потребность в физической активности (1-5).
    """

    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(max_length=200)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    friendliness = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    trainability = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    shedding_amount = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    exercise_needs = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )

    def __str__(self):
        return self.name
