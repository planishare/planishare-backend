from rest_framework import generics, permissions
from .models import Like, Download
from .serializers import DownloadSerializer, LikeSerializer
from api.permissions import isOwner

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]


class DownloadCreateAPIView(generics.CreateAPIView):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]