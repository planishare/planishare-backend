from django.contrib import admin
from .models import Subject, AcademicYear, Axis, Post

# Register your models here.
admin.site.register(Subject)
admin.site.register(AcademicYear)
admin.site.register(Axis)
admin.site.register(Post)
