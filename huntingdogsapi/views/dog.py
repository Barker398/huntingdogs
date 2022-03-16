from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from huntingdogsapi.models import Dog

class DogView(ViewSet):
    """Viewset Dogs"""
    def list(self, request):
        """List Dogs"""
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True,  context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """GET request for single Dog"""
        try:
            dog = Dog.objects.get(pk=pk)
            serializer = DogSerializer(dog, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
class DogSerializer(serializers.ModelSerializer):
    """Serializer data for Dogs"""
    class Meta:
        model = Dog
        fields = ('id', 'name', 'image_url', 'breed', 'kennel', 'traits')    