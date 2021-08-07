from rest_framework import serializers
from profiles_api import models


class UserProfileSerializers(serializers.ModelSerializer):
    """ Serializes A User Profile Object. """
    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {
            'write_only': True,
            'style': {'input_type': 'password'}
        }}

    def create(self, validated_data):
        """ Creates A New User Profile. """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'])

        return user
