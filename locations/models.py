from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    number = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return f'{self.number} - {self.name}';

class Commune(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='communes')

    def __str__(self) -> str:
        return self.name;