from rest_framework import generics, filters
from .models import AcademicLevel, Axis, Subject, Post
from .serializers import \
    AcademicLevelSerializer, \
    AxisSerializer, \
    SubjectSerializer, \
    PostDetailSerializer, \
    PostCreateSerializer, \
    PostUpdateSerializer

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class AcademicLevelListAPIView(generics.ListAPIView):
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer

class AxisListAPIView(generics.ListAPIView):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer

class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'title',
        'academic_level__name',
        'axis__name',
        'axis__subject__name'
    ]
    filterset_fields = ['user__id', 'academic_level__id', 'axis__id', 'axis__subject__id']

class PostMostLikedListAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]
    serializer_class = PostDetailSerializer

class PostMostDownloadedListAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(num_downloads=Count('downloads')).order_by('-num_downloads')[:10]
    serializer_class = PostDetailSerializer

class PostLatestListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-created_at')[:10]
    serializer_class = PostDetailSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
