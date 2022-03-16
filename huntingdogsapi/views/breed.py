from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from huntingdogsapi.models import Breed

class BreedView(ViewSet):
    """List Breeds of Dogs
    """
    def list(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            breed = Breed.objects.get(pk=pk)
            serializer = BreedSerializer(breed, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'breed_type', 'hunting_type')