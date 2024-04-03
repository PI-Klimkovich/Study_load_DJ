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

    # Действия
    # actions = ["title_up"]

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
#
#     @admin.action(description="Upper Title")
#     def title_up(self, form, queryset: QuerySet[LoadInfo]):
#         queryset.update(title=Upper(F("title")))
#
#     @admin.display(description="Содержимое")
#     def short_content(self, obj: LoadInfo) -> str:
#         return obj.content[:50]+"..."
#
#     @admin.display(description="Теги")
#     def tags_function(self, obj: LoadInfo) -> str:
#         tags = list(obj.tags.all())
#         text = ""
#         for tag in tags:
#             text += f"<span style=\"color: blue;\">{tag}</span><br>"
#         return mark_safe(text)
#
#     @admin.display(description="IMG")
#     def preview_image(self, obj: LoadInfo) -> str:
#         if obj.image:
#             return mark_safe(f'<img src="{obj.image.url}" height="100" />')
#         return ")("


@admin.register(OnDate)
class OnDateAdmin(admin.ModelAdmin):
    list_display = ["on_date"]


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
    # date_hierarchy = "on_date"
    print(1, OnDate.on_date)

    list_filter = [
        # "academic_year",
        "on_date",
        # "form_study",
        # "load_info__semester"
    ]
