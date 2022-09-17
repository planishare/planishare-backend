from django.contrib import admin

from api.models import LoginLog

# Register your models here.
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'created_at')
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id','created_at')
        return ()

admin.site.register(LoginLog, LoginLogAdmin)
