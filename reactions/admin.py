from django.contrib import admin
from .models import Like, Download

class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post__title', 'post__id', 'user__email', 'created_at') # list table
    readonly_fields=('created_at',) # edit form
    list_per_page = 10

    def user__email(self, obj):
        return obj.user.email

    def post__title(self, obj):
        return obj.post.title

    def post__id(self, obj):
        return obj.post.id

# Register your models here.
admin.site.register(Like, ReactionAdmin)
admin.site.register(Download, ReactionAdmin)
