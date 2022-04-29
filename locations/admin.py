from django.contrib import admin

from admin_auto_filters.filters import AutocompleteFilterFactory

from locations.models import Commune, Region

class RegionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'id')
    readonly_fields=('id',)
    search_fields = ['name']

class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name','region', 'id')
    readonly_fields=('id',)
    list_per_page = 10
    search_fields = ['name']

    # Automcomplete select form
    autocomplete_fields = ['region']

    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('Region', 'region'),
    ]

    def subject__name(self, obj):
        return obj.subject.name

admin.site.register(Region, RegionAdmin)
admin.site.register(Commune, CommuneAdmin)
