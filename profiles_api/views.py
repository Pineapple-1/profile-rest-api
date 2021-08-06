from django.http import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """retruns a list of apiview"""
        an_apiView = [
            'wtf is this i dont understad',
            'so to understand this i im doing this'
        ]
        return Response({'message':'helo','apiView':an_apiView})
    
    def post(self,request):
        
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self,request,pk=None):
        """handles updating an object """
        return Response ({'method': 'PUT' })

    def patch(self,request,pk=None):
        """handles partial updating an object """
        return Response ({'method': 'PATCH' })


    def delete(self,request,pk=None):
        """handles deletion of an object """
        return Response ({'method': 'DELETE' }) 
        
         
            
        
        