from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers to accept the post data """
    name = serializers.CharField(max_length = 12)