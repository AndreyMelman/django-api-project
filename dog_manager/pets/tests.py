from rest_framework.test import APITestCase
from rest_framework import status
from .models import Dog, Breed


class DogAPITestCase(APITestCase):
    def setUp(self):
        self.breed = Breed.objects.create(
            name="Labrador",
            size="Large",
            friendliness=5,
            trainability=5,
            shedding_amount=3,
            exercise_needs=5,
        )
        self.dog = Dog.objects.create(
            name="Buddy",
            age=3,
            breed=self.breed,
            gender="Male",
            color="Brown",
            favorite_food="Chicken",
            favorite_toy="Ball",
        )

    def test_create_dog(self):
        data = {
            "name": "Charlie",
            "age": 2,
            "breed": self.breed.id,
            "gender": "Male",
            "color": "Black",
            "favorite_food": "Beef",
            "favorite_toy": "Rope",
        }
        response = self.client.post("/api/dogs/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_dogs(self):
        response = self.client.get("/api/dogs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_dog_detail(self):
        response = self.client.get(f"/api/dogs/{self.dog.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.dog.name)

    def test_delete_dog(self):
        response = self.client.delete(f"/api/dogs/{self.dog.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dog.objects.count(), 0)


class BreedAPITestCase(APITestCase):
    def test_create_breed(self):
        data = {
            "name": "Beagle",
            "size": "Medium",
            "friendliness": 5,
            "trainability": 4,
            "shedding_amount": 3,
            "exercise_needs": 4,
        }
        response = self.client.post("/api/breeds/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_breeds(self):
        Breed.objects.create(
            name="Beagle",
            size="Medium",
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=4,
        )
        response = self.client.get("/api/breeds/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
