from django.urls import path
from api.authentication import FirebaseAuth
from api.permissions import IsAuthOrFirebaseAnon, IsUserProfile, IsOwner
from rest_framework.permissions import IsAuthenticated

from api.views import CheckStatus, RegisterAPIView
from locations.views import RegionWithCommunesListAPIView
from occupations.views import InstitutionListAPIView, EducationtListAPIView
from reports.views import ReportCreateAPIView
from users.views import IsEmailAvailable, UserDetailAPIView, UserDetailByEmailAPIView, UserUpdateAPIView
from posts.views import (
    AcademicLevelListAPIView,
    AxisListAPIView,
    SubjectListAPIView,
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    SubjectWithAxisListAPIView
)
from reactions.views import LikeCreateAPIView, LikeDeleteAPIView, ToggleLikeAPIView, ViewCreateAPIView

def public(route, api_view, name=None):
    '''
    Creates a public route.
    '''
    route = 'public/' + route
    return path(route, api_view.as_view(), name=name)

def protected(route, api_view, extra_permissions=[], must_auth=True, name=None):
    '''
    Creates a protected route using FirebaseAuth as default authentication class.
    '''

    # If not must_auth allow no authentication
    prefix = 'protected/' if must_auth else 'protected/allow-no-auth/'
    route = prefix + route

    authentication_classes = [FirebaseAuth]
    permission_classes = ([IsAuthenticated] if must_auth else []) + extra_permissions

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
    public('auth/register/', RegisterAPIView, name='register-user'),

    # Ocupations
    public('educations/', EducationtListAPIView, name='list-educations'),
    public('institutions/', InstitutionListAPIView, name='list-institutions'),

    # Locations
    public('regions-with-communes/', RegionWithCommunesListAPIView, name='list-regions-communes'),
    
    # Users
    # public('users/<int:pk>/', UserDetailAPIView, name='detail-user'),
    protected('users/by-email/<str:email>/', UserDetailByEmailAPIView, extra_permissions=[IsUserProfile], name='detail-user-by-email'),
    protected('users/update/<int:pk>/', UserUpdateAPIView, extra_permissions=[IsUserProfile], name='update-user'),
    public('users/is-email-available/<str:email>/', IsEmailAvailable, name='is-email-available'),
    
    # Posts
    public('academic-levels/', AcademicLevelListAPIView, name='list-academic-levels'),
    public('axis/', AxisListAPIView, name='list-axis'),
    public('subjects/', SubjectListAPIView, name='list-subjects'),
    public('subjects-with-axis/', SubjectWithAxisListAPIView, name='list-subjects-axis'),
    
    protected('posts/', PostListAPIView, must_auth=False, name='list-posts'),
    protected('posts/create/', PostCreateAPIView, extra_permissions=[IsOwner],  name='create-posts'),
    protected('posts/<int:pk>/', PostDetailAPIView, must_auth=False, name='detail-posts'),
    protected('posts/delete/<int:pk>/', PostDeleteAPIView, extra_permissions=[IsOwner], name='delete-posts'),
    protected('posts/update/<int:pk>/', PostUpdateAPIView, extra_permissions=[IsOwner], name='update-posts'),

    # Reactions
    protected('likes/create/', LikeCreateAPIView, extra_permissions=[IsOwner], name='create-like'),
    protected('likes/delete/<int:pk>/', LikeDeleteAPIView, extra_permissions=[IsOwner], name='delete-like'),
    protected('likes/toggle/', ToggleLikeAPIView, name='toggle-like'), # TODO: Refactor this to use permissions
    protected('views/create/', ViewCreateAPIView, name='create-view'), # TODO: Refactor this to use permissions
    
    # Reports
    protected('report/create/', ReportCreateAPIView, extra_permissions=[IsOwner], name='create-report'),

    # Check status
    path('status', CheckStatus.as_view(), name='check-status'),
]
