from django.db import models
from posts.models import Post
from users.models import User

class ReportType(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name;

class Report(models.Model):
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE, related_name='reports')
    # Created by
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reports_created', null=True)

    user_reported = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)
    post_reported = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports', blank=True, null=True)

    active = models.BooleanField(default=True)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'({self.id}) {self.report_type}';
