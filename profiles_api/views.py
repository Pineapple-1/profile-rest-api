
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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
    
    
    
    
    
class HeloViewSet (viewsets.ViewSet):
    """Test View Api"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ Return a helo world message """
        viewset = [
            'wtf is this i dont understad',
            'so to understand this i im doing this'
        ]
        return Response({'message':'helo','Viewset':viewset})
    
    def create(self,request ):
        """Create a new helo message"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def retrieve(self,request, pk= None):
        """handles getting object by its id"""
        return Response({'http_method':"GET"})
    
    def update(self,request, pk= None):
        """handles update by its id"""
        return Response({'http_method':"PUT"})
    
    def partialUpdate(self,request, pk= None):
        """handles partial update its id"""
        return Response({'http_method':"PATCH"})
    
    def destroy(self,request, pk= None):
        """handles removing an object"""
        return Response({'http_method':"del"})        
        
        
         
            
        
        