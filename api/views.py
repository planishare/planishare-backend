from rest_framework import generics
from users.models import User
from .serializers import RegisterUserSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = []