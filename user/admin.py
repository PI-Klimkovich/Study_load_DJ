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
        'is_member',
        'is_active',
        'email',
        'phone',
        'birthday',
        "is_staff",
        "is_superuser",
    ]
    search_fields = ['username', 'last_name']
    actions = ["block_user", "unlock_user", "block_member", "unlock_member"]
    list_editable = ("is_active", 'is_member',)
    readonly_fields = ["preview_image"]
    list_per_page = 10

    list_filter = [
        "is_member",
        "is_active",
        "is_superuser",
        "is_staff",
    ]

    @admin.action(description='Not is member')
    def block_member(self, request, queryset):
        queryset.update(is_member=False)

    @admin.action(description='Is member')
    def unlock_member(self, request, queryset):
        queryset.update(is_member=True)

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
                    "is_member",
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
    list_display = ["assignment_date", "user", "job_title", "academic_degree", "academic_title", "short_name"]
    list_per_page = 10
    # search_fields = ['user', 'assignment_date']

    list_filter = [
        "user",
        # "titles_name",
        # "user__is_member",
    ]

    @admin.display(description="ФИО преподавателя")
    def short_name(self, obj: Titles) -> str:
        return obj.user.last_name + ' ' + obj.user.first_name[0] + '.' + obj.user.middle_name[0] + '.'

    # @admin.display(description="Преподаватели")
    # def titles_name(self, obj: Titles) -> str:
    #     if obj.user.is_member:
    #         return obj.user
