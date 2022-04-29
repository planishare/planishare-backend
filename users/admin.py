from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

from admin_auto_filters.filters import AutocompleteFilterFactory

class CustomUserAdmin(UserAdmin):

    # Fields origianales de UserAdmin modificados, se muestran el editar usuario end /admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", 
            {
                "fields": (
                "first_name",
                "last_name",
                "education",
                "institution"
                )
            }
        ),
        ("Important dates", {"fields": ("created_at", "updated_at", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        # ("Important dates", {"fields": ("last_login", "date_joined", "created_at", "updated_at")}),
    )
    readonly_fields=('created_at', 'updated_at')

    # Campos que se mostrarán desde /admin al crear un nuevo usuario
    # En este caso deja el email en vez del username para crear un usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    # Busqueda en /admin
    search_fields = ('email',)
    ordering = ('email',)

    # Lista en /admin
    list_display = ('email', 'is_staff', 'is_active',)

    list_per_page = 10

    search_fields = ['email']

    # Automcomplete select form
    autocomplete_fields = ['institution']

    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('Institution', 'institution'),

        # Regular filter
        'education',
    ]


# Register your models here.
admin.site.register(User, CustomUserAdmin)