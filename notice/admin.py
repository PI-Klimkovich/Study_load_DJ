from django.contrib import admin
from .models import Notice
from user.models import User


class IsMemberUserFilter(admin.SimpleListFilter):
    title = "Преподаватели"
    parameter_name = "is_member"

    def lookups(self, request, model_admin):
        qs = User.objects.filter(is_member=True)
        return (
            (u.username, u.__str__) for u in qs
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__username=self.value())
        return queryset


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["message", "mod_time", "user", "created_at"]
    search_fields = ["message"]
    date_hierarchy = "mod_time"

    list_filter = [
        IsMemberUserFilter,
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
