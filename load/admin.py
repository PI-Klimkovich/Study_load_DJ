from django.contrib import admin

# from django.utils.safestring import mark_safe
# from django.db.models import QuerySet, F
# from django.db.models.functions import Upper

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
    # date_hierarchy = "on_date"

    # Поля, которые не имеют большого кол-ва уникальных вариантов!
    list_filter = [
        "academic_year",
        "semester",
        "form_study",
        # "load_info__semester"
    ]

    # filter_horizontal = ["form_study"]

    # readonly_fields = ["preview_image"]

    # fieldsets = (
    #     # 1
    #     (None, {"fields": ("academic_year", "faculty", "semester", "form_study", "discipline", "course_study", "group")}),
    #     ("Содержимое", {"fields": ("academic_year",)})
    # )
#
#     def get_queryset(self, request):
#         return (
#             LoadInfo.objects.all()
#             .select_related("academic_year")  # Вытягивание связанных данных из таблицы User в один запрос
#             .prefetch_related("tags")  # Вытягивание связанных данных из таблицы Tag в отдельные запросы
#         )


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
    # date_hierarchy = "on_date"

    list_filter = [
        "load_info__academic_year",
        "on_date",
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

