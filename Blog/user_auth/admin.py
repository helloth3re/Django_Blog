from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class UserModelAdmin(UserAdmin):
    list_display = ["id", "email", "is_active", "is_superuser",
                    "is_staff", "is_author", "is_reader"]
    list_filter = ["is_superuser"]

    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "is_author", "is_reader"]}),
        (_("Important dates"), {"fields": ("last_login",)}),
    ]

    # ✅ Add this to handle the add user form
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
            "email", "password1", "password2", "is_active", "is_staff", "is_superuser", "is_author", "is_reader"),
        }),
    )

    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(CustomUser, UserModelAdmin)
