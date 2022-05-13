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
        return f'{self.user} -> {self.post}';

class View(models.Model):
    # Use firebase uid like oHG6J95Z4gXc7aBJpxpsNqaQ2xz1
    firebaseUserId = models.CharField(null=False, blank=False, max_length=100);
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('firebaseUserId', 'post') 

    def __str__(self) -> str:
        return f'{self.firebaseUserId} -> {self.post}';
