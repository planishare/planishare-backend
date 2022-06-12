from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilterFactory

from reports.models import Report, ReportType

class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)
    list_per_page = 10
    search_fields = ['name']

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'id', 'user', 'active', 'created_at')
    readonly_fields=('id', 'created_at')
    list_per_page = 10
    
    # Automcomplete select form
    autocomplete_fields = ['report_type', 'user', 'user_reported', 'post_reported']

    # Filters
    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('Report type', 'report_type'),
        AutocompleteFilterFactory('User', 'user'),
        AutocompleteFilterFactory('User reported', 'user_reported'),
        AutocompleteFilterFactory('Post reported', 'post_reported')
    ]


    def report_type(self, obj):
        return obj.report_type.name
    
    def total_likes(self, obj):
        print(obj.created_at)
        return obj.likes.count()

# Register your models here.
admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportAdmin)
