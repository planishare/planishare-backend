from django.contrib import admin
from .models import Education, Institution, InstitutionType

# Register your models here.
admin.site.register(Education)
admin.site.register(Institution)
admin.site.register(InstitutionType)