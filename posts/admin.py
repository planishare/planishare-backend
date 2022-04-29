from django.contrib import admin
from .models import Subject, AcademicLevel, Axis, Post

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)
    list_per_page = 10

class AcedemicLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)
    list_per_page = 10

class AxisAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','subject__name')
    readonly_fields=('id',)
    list_per_page = 10

    def subject__name(self, obj):
        return obj.subject.name

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'academic_level', 'subject__name', 'axis', 'total_likes', 'total_downloads', 'id')
    readonly_fields=('id', 'created_at', 'updated_at')
    list_per_page = 10

    def subject__name(self, obj):
        return obj.axis.subject.name
    
    def total_likes(self, obj):
        print(obj.created_at)
        return obj.likes.count()
    
    def total_downloads(self, obj):
        return obj.downloads.count()

# Register your models here.
admin.site.register(Subject, SubjectAdmin)
admin.site.register(AcademicLevel, AcedemicLevelAdmin)
admin.site.register(Axis, AxisAdmin)
admin.site.register(Post, PostAdmin)
