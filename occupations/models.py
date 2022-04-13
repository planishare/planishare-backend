from django.db import models

class Education(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name;

class InstitutionType(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self) -> str:
        return self.name;

class Institution(models.Model):
    name = models.CharField(max_length=255, blank=False)
    institution_type = models.ForeignKey(InstitutionType, on_delete=models.CASCADE, related_name='institutions')
    def __str__(self) -> str:
        return self.name;

