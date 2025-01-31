from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, StudentAchievement

class CustomUserAdmin(UserAdmin):
    list_display = ("email", "name", "role", "is_active", "is_staff", "student_achievement")
    search_fields = ("email", "name", "role")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "role", "student_achievement")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "role", "student_achievement"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "school_name", "achievements")
    search_fields = ("name", "school_name")