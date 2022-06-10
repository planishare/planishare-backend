from django.db import models
from users.models import User
from posts.models import Post

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post') 

    def __str__(self) -> str:
        return f'{self.user} -> {self.post}'

class View(models.Model):
    # Use firebase uid like oHG6J95Z4gXc7aBJpxpsNqaQ2xz1
    firebase_user_id = models.CharField(null=False, blank=False, max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_views')
    first_seen = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('firebase_user_id', 'post') 

    def __str__(self) -> str:
        return f'{self.firebase_user_id} -> {self.post}'
