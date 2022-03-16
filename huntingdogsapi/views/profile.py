from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from huntingdogsapi.models import Profile

class ProfileView(ViewSet):
    """Profile views"""
    def list(self, request):
        """Profile"""
        profile = Profile.objects.get(user=request.auth.user)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """GET single profile object"""
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
class UserSerializer(serializers.ModelSerializer):
    """Serializer for User"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        
class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile"""
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'address', 'phoneNumber', 'email')
        