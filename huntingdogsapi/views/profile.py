from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from huntingdogsapi.models import Profile


class ProfileView(ViewSet):
    """Profile views"""

    def list(self, request):
        """Profile"""
        profile = Profile.objects.get(user=request.auth.user)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        profile = Profile()
        profile.bio = request.data["bio"]
        profile.address = request.data["address"]
        profile.phoneNumber = request.data["phoneNumber"]
        profile.email = request.data["email"]

        try:
            profile.save()
            serializer = ProfileSerializer(
                profile, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """GET single profile object"""
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(
                profile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        profile = Profile.objects.get(pk=pk)
        profile.bio = request.data["bio"]
        profile.address = request.data["address"]
        profile.phoneNumber = request.data["phoneNumber"]
        profile.email = request.data["email"]
        profile.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile"""
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'address',
                  'phoneNumber', 'email', 'favorites')
        depth = 2
