from django.db import models

from posts.models import Post
from users.models import User

# TODO: Create a new module called logs and add this logic there
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_logs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'({self.id}){self.user}'