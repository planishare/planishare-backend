from django.urls import path, include
from occupations.views import InstitutionListAPIView, EducationtListAPIView
from users.views import RegisterListAPIView, UserDetailAPIView, UserUpdateAPIView, UserUpdatePasswordAPIView
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

from .views import LoginView, CookieTokenRefreshView

urlpatterns = [
    # JWT
    path('login/', LoginView.as_view(), name='login'),
    path('login/token-refresh/', CookieTokenRefreshView.as_view(), name='login-token-refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Ocupations
    path('educations/', EducationtListAPIView.as_view(), name='list-educations'),
    path('institutions/', InstitutionListAPIView.as_view(), name='list-institutions'),
    
    # Users
    path('users/create/', RegisterListAPIView.as_view(), name='create-user'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='detail-user'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='update-user'),
    path('users/update-password/<int:pk>/', UserUpdatePasswordAPIView.as_view(), name='update-user-password'),
    
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