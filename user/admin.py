from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Titles


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = [
        'last_name',
        'first_name',
        'middle_name',
        'username',
        'is_active',
        'email',
        'phone',
        'birthday',
        "is_staff",
        "is_superuser",
    ]
    search_fields = ['username', 'last_name']
    date_hierarchy = "date_joined"
    actions = ["block_user", "unlock_user"]
    list_editable = ("is_active",)

    # @admin.display(description="Counts notes")
    # def count_note(self, obj):
    #     return obj.note_set.count()

    @admin.action(description='Block User')
    def block_user(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description='Unlock User')
    def unlock_user(self, request, queryset):
        queryset.update(is_active=True)

    fieldsets = (
        # 1  tuple(None, dict)
        (None, {"fields": ("username",)}),

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

