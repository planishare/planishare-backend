from rest_framework import generics, filters, permissions, pagination
from .models import AcademicLevel, Axis, Subject, Post
from .serializers import (
    AcademicLevelSerializer,
    AxisSerializer,
    SubjectSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
    SubjectWithAxisSerializer
)

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import isOwner
from api.utils import CustomPageNumberPagination
from django.db.models import F, When, Case
from django.db.models.lookups import GreaterThan, LessThanOrEqual

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

class SubjectWithAxisListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectWithAxisSerializer
    authentication_classes = []

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    
    serializer_class = PostDetailSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = [
        'title',
        'academic_level__name',
        'axis__name',
        'axis__subject__name'
    ]
    filterset_fields = ['user__id', 'academic_level__id', 'axis__id', 'axis__subject__id']
    ordering_fields = ['total_likes', 'total_views', 'created_at']

    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostMostLikedListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-total_likes')[:10]
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostMostViewedListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-total_views')[:10]
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostMostPopularListAPIView(generics.ListAPIView):
    queryset = Post.objects \
        .annotate(popular=Case(
            When(LessThanOrEqual(F('total_likes'), F('total_views')), then=F('total_likes')*65 + F('total_views')*35),
            When(GreaterThan(F('total_likes'), F('total_views')), then=F('total_views')*100)
        )) \
        .order_by('-popular')[:10]
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostLatestListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-created_at')[:10]
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]