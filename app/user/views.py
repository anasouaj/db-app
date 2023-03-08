"""
view for the user API
"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializers,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """ create a new user in the system"""
    serializer_class = UserSerializers


class CreatTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serielizer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES

