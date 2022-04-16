from rest_framework import generics
from .models import Like, Download
from .serializers import DownloadSerializer, LikeSerializer

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class DownloadCreateAPIView(generics.CreateAPIView):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer