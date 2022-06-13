from django.contrib import admin
from .models import Education, Institution, InstitutionType

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

class InstitutionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    list_per_page = 10
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution_type__name', 'id')
    list_per_page = 10
    search_fields = ['name']
    list_filter = ['institution_type']

    def institution_type__name(self, obj):
        return obj.institution_type.name

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

# Register your models here.
admin.site.register(Education, EducationAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(InstitutionType, InstitutionTypeAdmin)