import os
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication
from rest_framework import exceptions
from firebase_admin import auth, initialize_app, credentials

from planishare.settings import BASE_DIR

User = get_user_model() # To use custom user seted in settings

cred = credentials.Certificate(os.path.join(BASE_DIR, 'firebase_config.json'))
initialize_app(cred)

# NOTE: Remove raise exceptions if you want to use another authentication method together with this one
class FirebaseAuth(authentication.BaseAuthentication):
    '''
    Authenticate user usign Firebase
    '''

    def authenticate(self, request):
        # Get auth header
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if not authorization_header:
            raise exceptions.AuthenticationFailed('Auth header not provided')

        # Get token
        token = authorization_header.split(" ").pop()
        if not token:
            raise exceptions.AuthenticationFailed('Auth token not provided')

        # Decode token
        try:
            decoded_token = auth.verify_id_token(token)
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)

        # If user is anonymous, then NO authenticate but pass decoded token
        if (decoded_token['firebase']['sign_in_provider'] == 'anonymous'):
            print('FirebaseAuth (Anon): ' + str(decoded_token))
            return (None, decoded_token)
        
        # If user exist in Planishare database, then authenticate and pass decoded token
        try:
            email = decoded_token.get("email")
            user = User.objects.get(email=email)
            print('FirebaseAuth (User): ' + str(decoded_token))
            return (user, decoded_token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found in Planishare database: " + email)
