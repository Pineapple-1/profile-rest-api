from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """serializers to accept the post data """
    name = serializers.CharField(max_length = 10)