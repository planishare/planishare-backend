import code
from rest_framework import generics, permissions
from .models import User
from .serializers import UserDetailSerializer, UserUpdateSerializer, UserUpdatePasswordSerializer
from api.permissions import isUserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from django.utils import timezone

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = []

class UserDetailByEmailAPIView(APIView):
    def get(self, request, email, format=None):
        try:
            user = User.objects.get(email=email)
            if user == request.user:
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return Response(UserDetailSerializer(user).data)
            data = {'detail': 'Invalid ID token or dont have permissions'}
            return Response(data, 403)
        except Exception:
            exc = exceptions.NotFound()
            data = {'detail': exc.detail}
            return Response(data, exc.status_code)

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