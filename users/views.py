from rest_framework import generics, permissions
from .models import User
from .serializers import UserDetailSerializer, UserUpdateSerializer, UserUpdatePasswordSerializer
from api.permissions import isUserProfile
from rest_framework.views import APIView
from rest_framework.response import Response

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

class IsEmailAvailable(APIView):
    authentication_classes = []

    def get(self, request, email, format=None):
        user = User.objects.filter(email=email);
        if (len(user)):
            return Response({"isAvailable": False})
        return Response({"isAvailable": True})