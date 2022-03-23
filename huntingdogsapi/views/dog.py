from dataclasses import fields
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from huntingdogsapi.models import Dog, Breed, Kennel, Trait, Profile


class DogView(ViewSet):
    """Viewset Dogs"""

    def list(self, request):
        """List Dogs"""
        dogs = Dog.objects.all()
        serializer = DogSerializer(
            dogs, many=True,  context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """GET request for single Dog"""
        try:
            dog = Dog.objects.get(pk=pk)
            serializer = DogSerializer(dog, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk=None):
        """Managing gamers signing up for events"""
        # Django uses the `Authorization` header to determine
        # which user is making the request to sign up
        profile = Profile.objects.get(user=request.auth.user)

        try:
            # Handle the case if the client specifies a game
            # that doesn't exist
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return Response(
                {'message': 'Dog does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # A gamer wants to sign up for an event
        if request.method == "POST":
            try:
                # Using the attendees field on the event makes it simple to add a gamer to the event
                # .add(gamer) will insert into the join table a new row the gamer_id and the event_id
                profile.favorites.add(dog)
                return Response({}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({'message': ex.args[0]})

        # User wants to leave a previously joined event
        elif request.method == "DELETE":
            try:
                # The many to many relationship has a .remove method that removes the gamer from the attendees list
                # The method deletes the row in the join table that has the gamer_id and event_id
                profile.favorites.remove(dog)
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            except Exception as ex:
                return Response({'message': ex.args[0]})


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('breed_type', 'hunting_type')


class KennelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kennel
        fields = ('id', 'name', 'image_url')


class Traitserializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ('id', 'description')


class DogSerializer(serializers.ModelSerializer):
    """Serializer data for Dogs"""
    class Meta:
        model = Dog
        fields = ('id', 'name', 'image_url', 'breed', 'kennel', 'traits')
        depth = 2
