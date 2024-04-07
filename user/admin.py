from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import User, Titles


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = [
        "preview_image",
        'username',
        'last_name',
        'first_name',
        'middle_name',
        'is_active',
        'email',
        'phone',
        'birthday',
        "is_staff",
        "is_superuser",
    ]
    search_fields = ['username', 'last_name']
    actions = ["block_user", "unlock_user"]
    list_editable = ("is_active",)
    readonly_fields = ["preview_image"]

    @admin.action(description='Block User')
    def block_user(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description='Unlock User')
    def unlock_user(self, request, queryset):
        queryset.update(is_active=True)

    @admin.display(description="Фото")
    def preview_image(self, obj: User) -> str:
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" height="100" />')
        return "}{"

    fieldsets = (
        # 1  tuple(None, dict)
        (None, {"fields": ("username", "preview_image",)}),

        # 2  tuple(str, dict)
        (
            "Персональная информация",
            {
                "fields": (
                    'last_name',
                    'first_name',
                    'middle_name',
                    'birthday',
                    'email',
                    'phone',
                    'address',
                    'photo',
                    'description',
                ),
            },
        ),

        # 3  tuple(str, dict)
        (
            "Права пользователя",
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

        # 4  tuple(str, dict)
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ["assignment_date", "user", "job_title", "academic_degree", "academic_title"]