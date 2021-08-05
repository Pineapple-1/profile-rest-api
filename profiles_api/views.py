from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    
    def get(self, request, format=None):
        """retruns a list of apiview"""
        an_apiView = [
            'wtf is this i dont understad',
            'so to understand this i im doing this'
        ]
        
        return Response({'message':'helo','apiView':an_apiView})