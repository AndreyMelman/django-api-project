from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogListSerializer, DogDetailSerializer, BreedSerializer
from django.db.models import Avg, Count, OuterRef, Subquery


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer
    detail_serializer_class = DogDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            avg_age_subquery = (
                Breed.objects.filter(pk=OuterRef("breed_id"))
                .annotate(avg_age=Avg("dogs__age"))
                .values("avg_age")[:1]
            )
            queryset = queryset.annotate(avg_breed_age=Subquery(avg_age_subquery))
        elif self.action == "retrieve":
            same_breed_count_subquery = (
                Dog.objects.filter(breed=OuterRef("breed_id"))
                .values("breed")
                .annotate(count=Count("id"))
                .values("count")[:1]
            )
            queryset = queryset.annotate(
                same_breed_count=Subquery(same_breed_count_subquery)
            )
        return queryset


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        if self.action == "list":
            return Breed.objects.annotate(dogs_count=Count("dogs"))
        return super().get_queryset()
