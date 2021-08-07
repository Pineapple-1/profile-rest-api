from rest_framework import viewsets
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication


class UserProfileViewSet(viewsets.ModelViewSet):
    """Test View Api"""
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
