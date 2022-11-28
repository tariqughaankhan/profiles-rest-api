from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class HelloApiView (APIView):

    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):


        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    def post(self, request ):

         serializer=self.serializer_class(data=request.data)
         if serializer.is_valid():
             name=serializer.validated_data.get('name')
             message=f'hello {name}'
             return Response({'message':message})
         else:
             return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
             )

    def put(request,pk=None):
         return Response({'methods':'PUT'})
    def patch(request,pk=None):
         return Response({'methods':'PATCH'})
    def delete(request,pk=None):
         return Response({'methods':'Delete'})
class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        as_data=[
        'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'helo','as_data':as_data})
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backend=(filters.SearchFilter,)
    search_fields=('name','email',)
class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
