from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["message", "mod_time", "user", "created_at"]
    search_fields = ["message"]
    date_hierarchy = "mod_time"

    list_filter = [
        "user",
        # "user__email"
    ]

    fieldsets = (
        # 1
        (None, {"fields": ("message", "user")}),
    )

    def get_queryset(self, request):
        return (
            Notice.objects.all()
            .select_related("user")  # Вытягивание связанных данных из таблицы User в один запрос
        )
