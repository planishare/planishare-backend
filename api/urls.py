from django.urls import path
from api.authentication import FirebaseAuth
from api.permissions import IsAuthOrFirebaseAnon, isUserProfile, isOwner
from rest_framework.permissions import IsAuthenticated

from api.views import CheckStatus, RegisterAPIView
from locations.views import RegionWithCommunesListAPIView
from occupations.views import InstitutionListAPIView, EducationtListAPIView
from reports.views import ReportCreateAPIView
from users.views import IsEmailAvailable, UserDetailAPIView, UserDetailByEmailAPIView, UserUpdateAPIView
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
from reactions.views import LikeCreateAPIView, LikeDeleteAPIView, ToggleLikeAPIView, ViewCreateAPIView

def protected(route, api_view, extra_permissions=[], allow_anon=False, name=None):
    '''
    Creates a protected route for authenticated or anonymous Firebase users.
    '''
    prefix = 'protected/' if not allow_anon else 'protected/a/'
    route = prefix + route

    authentication_classes = [FirebaseAuth]
    permission_classes = [IsAuthOrFirebaseAnon if allow_anon else IsAuthenticated]
    permission_classes = permission_classes + extra_permissions

    return path(
        route,
        api_view.as_view(
            authentication_classes=authentication_classes,
            permission_classes=permission_classes
        ),
        name=name
    )

urlpatterns = [
    # Authentication
    protected('auth/register/', RegisterAPIView, allow_anon=True, name='register-user'),

    # Ocupations
    protected('educations/', EducationtListAPIView, allow_anon=True, name='list-educations'),
    protected('institutions/', InstitutionListAPIView, allow_anon=True, name='list-institutions'),

    # Locations
    protected('regions-with-communes/', RegionWithCommunesListAPIView, allow_anon=True, name='list-regions-communes'),
    
    # Users
    protected('users/<int:pk>/', UserDetailAPIView, allow_anon=True, name='detail-user'),
    protected('users/by-email/<str:email>/', UserDetailByEmailAPIView, name='detail-user-by-email'),
    protected('users/update/<int:pk>/', UserUpdateAPIView, extra_permissions=[isUserProfile], name='update-user'),
    protected('users/is-email-available/<str:email>/', IsEmailAvailable, allow_anon=True, name='is-email-available'),
    
    # Posts
    protected('academic-levels/', AcademicLevelListAPIView, allow_anon=True, name='list-academic-levels'),
    protected('axis/', AxisListAPIView, allow_anon=True, name='list-axis'),
    protected('subjects/', SubjectListAPIView, allow_anon=True, name='list-subjects'),
    protected('subjects-with-axis/', SubjectWithAxisListAPIView, allow_anon=True, name='list-subjects-axis'),
    
    protected('posts/', PostListAPIView, allow_anon=True, name='list-posts'),
    protected('posts/create/', PostCreateAPIView, extra_permissions=[isOwner],  name='create-posts'),
    protected('posts/<int:pk>/', PostDetailAPIView, allow_anon=True, name='detail-posts'),
    protected('posts/delete/<int:pk>/', PostDeleteAPIView, extra_permissions=[isOwner], name='delete-posts'),
    protected('posts/update/<int:pk>/', PostUpdateAPIView, extra_permissions=[isOwner], name='update-posts'),

    # Reactions
    protected('likes/create/', LikeCreateAPIView, extra_permissions=[isOwner], name='create-like'),
    protected('likes/delete/<int:pk>/', LikeDeleteAPIView, extra_permissions=[isOwner], name='delete-like'),
    protected('likes/toggle/', ToggleLikeAPIView, name='toggle-like'), # TODO: Refactor this to use permissions
    protected('views/create/', ViewCreateAPIView, name='create-view'), # TODO: Refactor this to use permissions
    
    # Reports
    protected('report/create/', ReportCreateAPIView, extra_permissions=[isOwner], name='create-report'),

    # Check status
    path('status', CheckStatus.as_view(), name='check-status'),
]
