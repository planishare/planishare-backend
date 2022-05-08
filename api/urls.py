from django.urls import path
from api.views import RegisterAPIView
from occupations.views import InstitutionListAPIView, EducationtListAPIView
from users.views import IsEmailAvailable, UserDetailAPIView, UserUpdateAPIView, UserUpdatePasswordAPIView
from posts.views import (
    AcademicLevelListAPIView,
    AxisListAPIView,
    SubjectListAPIView,
    PostListAPIView,
    PostMostLikedListAPIView,
    PostMostDownloadedListAPIView,
    PostLatestListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
)
from reactions.views import LikeCreateAPIView, DownloadCreateAPIView

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterAPIView.as_view(), name='register-user'),

    # Ocupations
    path('educations/', EducationtListAPIView.as_view(), name='list-educations'),
    path('institutions/', InstitutionListAPIView.as_view(), name='list-institutions'),
    
    # Users
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='detail-user'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='update-user'),
    path('users/update-password/<int:pk>/', UserUpdatePasswordAPIView.as_view(), name='update-user-password'),

    path('users/is-email-available/<str:email>/', IsEmailAvailable.as_view(), name='is-email-available'),
    
    # Posts
    path('academic-levels/', AcademicLevelListAPIView.as_view(), name='list-academic-levels'),
    path('axis/', AxisListAPIView.as_view(), name='list-axis'),
    path('subjects/', SubjectListAPIView.as_view(), name='list-subjects'),
    path('posts/', PostListAPIView.as_view(), name='list-posts'),
    path('posts/most-liked/', PostMostLikedListAPIView.as_view(), name='list-most-liked-posts'),
    path('posts/most-downloaded/', PostMostDownloadedListAPIView.as_view(), name='list-most-downloaded-posts'),
    path('posts/latest/', PostLatestListAPIView.as_view(), name='list-latest-posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name='create-posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='detail-posts'),
    path('posts/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='delete-posts'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name='update-posts'),

    # Reactions
    path('likes/create/', LikeCreateAPIView.as_view(), name='create-like'),
    path('downloads/create/', DownloadCreateAPIView.as_view(), name='create-download'),
]