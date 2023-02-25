from rest_framework import generics, views
from users.models import User
from .serializers import RegisterUserSerializer
from rest_framework.response import Response

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

class CheckStatus(views.APIView):
    def get(self, request, format=None):
        return Response({ "status": "ok" })