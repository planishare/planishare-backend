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

    def perform_destroy(self, instance):
        post = instance.post
        post.total_likes -= 1
        post.save()
        return super().perform_destroy(instance)

class ViewCreateAPIView(generics.CreateAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer