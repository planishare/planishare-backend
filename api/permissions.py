from rest_framework import permissions

class isOwner(permissions.BasePermission):
    """
    Allows obj access only to user owner.
    Only for models where owner field is called 'user'
    """

    # Check get, delete, patch, put request
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
        
    # Check post request
    def has_permission(self, request, view):
        if request.method == 'POST':
            try:
                userId = request.data['user']
                if userId is not None:
                    return request.user.id == int(userId)
            except:
                return False
        return True
        
# TODO: Use upper cammel case for classes
class isUserProfile(permissions.BasePermission):
    """
    Allows user obj access only to user owner.
    """

    # Check get, delete, patch, put request
    def has_object_permission(self, request, view, obj):
        return obj == request.user

    # Check post request
    def has_permission(self, request, view):
        if request.method == 'POST':
            try:
                userId = view.kwargs.get('pk')
                if userId is not None:
                    return request.user.id == int(userId)
            except:
                return False
        return True

class IsAuthOrFirebaseAnon(permissions.IsAuthenticated):
    """
     Allows obj access to Firebase anonymous user.
    """

    # Check post request
    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            return True
            
        if (request.auth):
            return request.auth['firebase']['sign_in_provider'] == 'anonymous'
        return False