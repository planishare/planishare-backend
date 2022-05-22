from django.urls import path
from api.views import RegisterAPIView
from locations.views import RegionWithCommunesListAPIView
from occupations.views import InstitutionListAPIView, EducationtListAPIView
from users.views import IsEmailAvailable, UserDetailAPIView, UserDetailByEmailAPIView, UserUpdateAPIView, UserUpdatePasswordAPIView
from posts.views import (
    AcademicLevelListAPIView,
    AxisListAPIView,
    PostMostPopularListAPIView,
    PostMostViewedListAPIView,
    SubjectListAPIView,
    PostListAPIView,
    PostMostLikedListAPIView,
    PostLatestListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    SubjectWithAxisListAPIView
)
from reactions.views import LikeCreateAPIView, LikeDeleteAPIView, ViewCreateAPIView

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterAPIView.as_view(), name='register-user'),

    # Ocupations
    path('educations/', EducationtListAPIView.as_view(), name='list-educations'),
    path('institutions/', InstitutionListAPIView.as_view(), name='list-institutions'),

    # Locations
    path('regions-with-communes/', RegionWithCommunesListAPIView.as_view(), name='list-regions-communes'),
    
    # Users
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='detail-user'),
    path('users/by-email/<str:email>/', UserDetailByEmailAPIView.as_view(), name='detail-user-by-email'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='update-user'),
    path('users/update-password/<int:pk>/', UserUpdatePasswordAPIView.as_view(), name='update-user-password'),

    path('users/is-email-available/<str:email>/', IsEmailAvailable.as_view(), name='is-email-available'),
    
    # Posts
    path('academic-levels/', AcademicLevelListAPIView.as_view(), name='list-academic-levels'),
    path('axis/', AxisListAPIView.as_view(), name='list-axis'),
    path('subjects/', SubjectListAPIView.as_view(), name='list-subjects'),
    path('subjects-with-axis/', SubjectWithAxisListAPIView.as_view(), name='list-subjects-axis'),
    path('posts/', PostListAPIView.as_view(), name='list-posts'),
    path('posts/most-liked/', PostMostLikedListAPIView.as_view(), name='list-most-liked-posts'),
    path('posts/most-viewed/', PostMostViewedListAPIView.as_view(), name='list-most-viewed-posts'),
    path('posts/popular/', PostMostPopularListAPIView.as_view(), name='list-popular-posts'),
    path('posts/latest/', PostLatestListAPIView.as_view(), name='list-latest-posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name='create-posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='detail-posts'),
    path('posts/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='delete-posts'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name='update-posts'),

    # Reactions
    path('likes/create/', LikeCreateAPIView.as_view(), name='create-like'),
    path('likes/delete/<int:pk>/', LikeDeleteAPIView.as_view(), name='delete-like'),
    path('views/create/', ViewCreateAPIView.as_view(), name='create-view'),
]