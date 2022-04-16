from django.db import models

from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name;

class Axis(models.Model):
    name = models.CharField(max_length=255, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='axis')

    def __str__(self) -> str:
        return self.name;

class AcademicLevel(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name;

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    image = models.CharField(max_length=255, blank=False)
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.SET_NULL, blank=False, null=True, related_name='academic_levels')
    axis = models.ForeignKey(Axis, on_delete=models.SET_NULL, blank=False, null=True, related_name='axis')
    main_file = models.CharField(max_length=255, blank=False)
    suporting_material = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user}: {self.title}';

