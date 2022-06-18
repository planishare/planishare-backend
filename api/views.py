from rest_framework import generics, views
from users.models import User
from .serializers import RegisterUserSerializer
from rest_framework.response import Response

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = []

class CheckStatus(views.APIView):
    authentication_classes = []

    def get(self, request, format=None):
        return Response({ "status": "ok" })