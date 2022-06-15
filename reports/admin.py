from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilterFactory

from reports.models import Report, ReportType

class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id')
        return ()

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'id', 'user', 'active', 'created_at')
    list_per_page = 10
    
    # Automcomplete select form
    autocomplete_fields = ['report_type', 'user', 'user_reported', 'post_reported']

    # Filters
    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('Report type', 'report_type'),
        AutocompleteFilterFactory('User', 'user'),
        AutocompleteFilterFactory('User reported', 'user_reported'),
        AutocompleteFilterFactory('Post reported', 'post_reported'),
        'active'
    ]


    def report_type(self, obj):
        return obj.report_type.name

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id', 'created_at')
        return ()

# Register your models here.
admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportAdmin)
