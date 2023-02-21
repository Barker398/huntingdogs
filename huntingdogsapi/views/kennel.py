from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from huntingdogsapi.models import Kennel


class KennelView(ViewSet):
    """List Kennels"""

    def list(self, request):
        """List Kennels"""
        kennels = Kennel.objects.all()
        serializer = KennelSerializer(
            kennels, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """GET request for single Kennel"""
        try:
            kennel = Kennel.objects.get(pk=pk)
            serializer = KennelSerializer(kennel, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class KennelSerializer(serializers.ModelSerializer):
    """Serializer data for a Kennel"""
    class Meta:
        model = Kennel
        fields = ('id', 'name', 'image_url', 'dogs')
        depth = 2
