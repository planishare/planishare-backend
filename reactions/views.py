from rest_framework import generics, permissions

from .models import Like, View
from .serializers import LikeSerializer, ViewSerializer
from api.permissions import isOwner

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class ViewCreateAPIView(generics.CreateAPIView):
    # TODO: Dont sent 404 when is already viewed
    queryset = View.objects.all()
    serializer_class = ViewSerializer