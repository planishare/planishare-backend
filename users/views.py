import code
from rest_framework import generics, permissions

from api.models import LoginLog
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

class UserDetailByEmailAPIView(APIView):
    def get(self, request, email, format=None):
        try:
            user = User.objects.get(email=email)
            if user == request.user:
                # Update user last login
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])

                # Create login log
                loginLog = LoginLog(user=user)
                loginLog.save()

                return Response(UserDetailSerializer(user).data)

            # TODO: Use exceptions
            data = {'detail': 'Invalid ID token or dont have permissions'}
            return Response(data, 403)
        except Exception:
            exc = exceptions.NotFound()
            data = {'detail': exc.detail}
            return Response(data, exc.status_code)

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class IsEmailAvailable(APIView):
    def get(self, request, email, format=None):
        user = User.objects.filter(email=email);
        if (len(user)):
            return Response({"isAvailable": False})
        return Response({"isAvailable": True})