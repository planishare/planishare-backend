from django.contrib import admin
from .models import Like, View
from admin_auto_filters.filters import AutocompleteFilterFactory

class LikeAdmin(admin.ModelAdmin):
    list_display = ('post__title', 'post__id', 'user__email', 'created_at') # list table
    list_per_page = 10

    # Automcomplete select form
    autocomplete_fields = ['post', 'user']

    list_filter = [
        AutocompleteFilterFactory('Post', 'post'),
        AutocompleteFilterFactory('User', 'user'),
        AutocompleteFilterFactory('Post owner', 'post__user'),
    ]

    def user__email(self, obj):
        return obj.user.email

    def post__title(self, obj):
        return obj.post.title

    def post__id(self, obj):
        return obj.post.id

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created_at',)
        return ()

class ViewAdmin(admin.ModelAdmin):
    list_display = ('post__title', 'post__id', 'firebase_user_id', 'user__email', 'first_seen') # list table
    list_per_page = 10
    
    # Automcomplete select form
    autocomplete_fields = ['post', 'user']

    list_filter = [
        AutocompleteFilterFactory('Post', 'post'),
        AutocompleteFilterFactory('Post owner', 'post__user'),
        AutocompleteFilterFactory('User', 'user'),
    ]

    def post__title(self, obj):
        return obj.post.title

    def post__id(self, obj):
        return obj.post.id
    
    def user__email(self, obj):
        if (obj.user):
            return obj.user.email
        return 'Anónimo'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('first_seen',)
        return ()

# Register your models here.
admin.site.register(Like, LikeAdmin)
admin.site.register(View, ViewAdmin)
