from rest_framework import generics, filters, permissions, pagination
from .models import AcademicLevel, Axis, Subject, Post
from .serializers import (
    AcademicLevelSerializer,
    AxisSerializer,
    SubjectSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostUpdateSerializer
)

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import isOwner
from api.utils import CustomPageNumberPagination

class AcademicLevelListAPIView(generics.ListAPIView):
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer
    authentication_classes = []

class AxisListAPIView(generics.ListAPIView):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer
    authentication_classes = []

class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = []

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects \
        .annotate(total_likes=Count('likes', distinct=True)) \
        .annotate(total_downloads=Count('downloads', distinct=True))
    
    serializer_class = PostDetailSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = [
        'title',
        'academic_level__name',
        'axis__name',
        'axis__subject__name'
    ]
    filterset_fields = ['user__id', 'academic_level__id', 'axis__id', 'axis__subject__id']
    ordering_fields = ['total_likes', 'total_downloads', 'created_at']

    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostMostLikedListAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')[:10]
    serializer_class = PostDetailSerializer
    authentication_classes = []

class PostMostDownloadedListAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(total_downloads=Count('downloads')).order_by('-total_downloads')[:10]
    serializer_class = PostDetailSerializer
    authentication_classes = []

class PostLatestListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-created_at')[:10]
    serializer_class = PostDetailSerializer
    authentication_classes = []

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    authentication_classes = []

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]
