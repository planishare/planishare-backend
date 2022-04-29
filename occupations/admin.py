from django.contrib import admin
from .models import Education, Institution, InstitutionType

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)
    list_per_page = 10

class InstitutionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields=('id',)
    list_per_page = 10

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution_type__name', 'id')
    readonly_fields=('id',)
    list_per_page = 10
    search_fields = ['name']

    def institution_type__name(self, obj):
        return obj.institution_type.name

# Register your models here.
admin.site.register(Education, EducationAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(InstitutionType, InstitutionTypeAdmin)