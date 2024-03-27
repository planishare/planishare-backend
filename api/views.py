from rest_framework import generics, views
from users.models import User
from .serializers import RegisterUserSerializer
from rest_framework.response import Response

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

class CheckStatus(views.APIView):
    def get(self, request, format=None):
        # Do request to also check database status
        latest_logged_user = User.objects.only('last_login').filter(last_login__isnull=False).order_by('-last_login').first()
        return Response({ "status": "ok", "latest_user_login": latest_logged_user.last_login })