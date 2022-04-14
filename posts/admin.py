from django.contrib import admin
from .models import Subject, AcademicLevel, Axis, Post

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)

class AcedemicLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)

class AxisAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','subject__name')
    readonly_fields=('id',)

    def subject__name(self, obj):
        return obj.subject.name

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'academic_level', 'subject__name', 'axis', 'id')
    readonly_fields=('id',)

    def subject__name(self, obj):
        return obj.axis.subject.name

# Register your models here.
admin.site.register(Subject, SubjectAdmin)
admin.site.register(AcademicLevel, AcedemicLevelAdmin)
admin.site.register(Axis, AxisAdmin)
admin.site.register(Post, PostAdmin)
