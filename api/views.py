from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .serializers import CookieTokenRefreshSerializer
class LoginView(TokenObtainPairView):

    # Set refreshToken in a cookie and delete it from response
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 1 # 1 days
            response.set_cookie(
                'refreshToken',
                response.data['refresh'],
                max_age=cookie_max_age,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    # Set refreshToken in a cookie and delete it from response
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 1 # 1 days
            response.set_cookie(
                'refreshToken',
                response.data['refresh'],
                max_age=cookie_max_age,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)