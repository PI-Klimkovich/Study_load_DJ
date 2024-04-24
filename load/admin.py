from django.contrib import admin
from .models import Load, LoadInfo, Discipline, Group, OnDate


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(LoadInfo)
class LoadInfoAdmin(admin.ModelAdmin):
    list_display = ["academic_year", "faculty", "semester", "form_study", "discipline", "course_study", "group"]
    search_fields = ["discipline", "group"]

    list_filter = [
        "academic_year",
        "semester",
        "form_study",
    ]

    # date_hierarchy = "on_date"
    # filter_horizontal = ["form_study"]
    # readonly_fields = ["preview_image"]


@admin.register(OnDate)
class OnDateAdmin(admin.ModelAdmin):
    list_display = ["on_date", "note"]


@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    list_display = [
        "load_info",
        "on_date",
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
    date_hierarchy = "on_date__on_date"

    list_filter = [
        "load_info__academic_year",
        # "on_date",
        "load_info__semester",
        "load_info__form_study",
    ]

    fieldsets = (
        # 1  tuple(None, dict)
        (None, {"fields": ("load_info", "on_date",)}),

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
