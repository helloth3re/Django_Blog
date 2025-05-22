from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class UserModelAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User
    list_display = ["id", "email", "is_active", "is_superuser",
                    "is_staff", "is_author", "is_reader"]
    list_filter = ["is_superuser"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "is_author", "is_reader"]})
    ]

    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(CustomUser, UserModelAdmin)