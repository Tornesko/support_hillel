from django.contrib import admin  # noqa:F401

from .models import Role, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["user_permissions", "groups"]
    readonly_fields = ["password", "last_login"]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
