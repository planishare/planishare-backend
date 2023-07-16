import email
from rest_framework import generics, permissions
from posts.models import Post

from users.models import User
from .models import Like, View
from .serializers import LikeSerializer, ViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_destroy(self, instance):
        post = instance.post
        post.total_likes -= 1
        post.save()
        return super().perform_destroy(instance)
    
class ToggleLikeAPIView(APIView):
    def post(self, request, format=None):
        # Validate body
        data = {}
        invalid_data = False
        try:
            userId = request.data['user']
        except KeyError:
            data['user'] = ["This field is required."]
            invalid_data = True
        try:
            postId = request.data['post']
        except KeyError:
            data['post'] = ["This field is required."]
            invalid_data = True
        if invalid_data:
            return Response(data, 400)

        # Get user and post
        try:
            user = User.objects.get(id=userId)
            post = Post.objects.get(id=postId)

            # Check if user has permission
            if user.email != request.user.email:
                exc = exceptions.PermissionDenied()
                data = {'detail': exc.detail}
                return Response(data, exc.status_code)
        except Exception:
            exc = exceptions.NotFound()
            data = {'detail': exc.detail}
            return Response(data, exc.status_code)

        try:
            # Delete like
            like = Like.objects.get(user=userId, post=postId)
            post.total_likes -= 1
            like.delete()
            post.save()
            return Response({ 'id': None }, 200)
        except Exception:
            # Create like
            like = Like(user=user, post=post)
            post.total_likes += 1
            like.save()
            post.save()
            return Response({ 'id': like.id }, 200)

class ViewCreateAPIView(generics.CreateAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer