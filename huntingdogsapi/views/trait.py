from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from huntingdogsapi.models import Trait

class TraitView(ViewSet):
    """Traits View"""
    def list(self, request):
        """List Traits"""
        traits = Trait.objects.all()
        serializer = TraitSerializer(traits, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """GET request for Traits"""
        try:
            trait = Trait.objects.get(pk=pk)
            serializer = TraitSerializer(trait, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
         
class TraitSerializer(serializers.ModelSerializer):
    """Serializer data"""
    class Meta:
        model = Trait
        fields = ('id', 'description')
        