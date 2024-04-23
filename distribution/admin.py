from django.contrib import admin

from .models import Distribution
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


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "load",
        "total",
        # "lectures",
        # "laboratory",
        # "practical",
        # "course_work",
        # "calculation_and_graphic_works",
        # "control",
        # "consultations",
        # "tests",
        # "exams",
        # "diploma",
        # "state_exam",
        # "practice",
        # "postgraduate_studies",
        "note",
    ]
    readonly_fields = ["total"]
    list_per_page = 10
    # date_hierarchy = "on_date"

    list_filter = [
        IsMemberUserFilter,
        "load__load_info__academic_year",
        "load__on_date",
        "load__load_info__semester",
        "load__load_info__form_study",
    ]

    fieldsets = (
        # 1  tuple(None, dict)
        (
            None,
            {
                "fields": (
                    "user",
                    # "load__on_date",
                    "load",
                )
            }
        ),

        # 2  tuple(str, dict)
        (
            "Детализация",
            {
                "fields": (
                    ("lectures", "laboratory", "practical",),
                    ("course_work", "calculation_and_graphic_works", "control",),
                    ("consultations", "tests", "exams",),
                    ("diploma", "state_exam",),
                    ("practice", "postgraduate_studies", "total",),
                    ("note",),
                ),
            },
        ),
    )
