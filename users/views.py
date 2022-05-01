from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterUserSerializer,UserDetailSerializer, UserUpdateSerializer, UserUpdatePasswordSerializer
from api.permissions import isUserProfile

class RegisterListAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = []

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = []

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, isUserProfile]

class UserUpdatePasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer