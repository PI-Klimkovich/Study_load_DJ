from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
import pandas as pd

from .models import Load
from user.models import User, Titles


def home_page_view(request):
    # all_users = User.objects.all().filter(is_member=True)  # Получение всех записей из таблицы этой модели.
    all_users = User.objects.prefetch_related().filter(is_member=True)
    users_titles = []
    for user in all_users:
        titles = user.titles_set.all().order_by("-assignment_date").first()
        titles_ = user.titles_set.all().order_by("assignment_date").first()
        users_titles.append(
            {
                'username': user.username,
                'last_name': user.last_name,
                'first_name': user.first_name,
                'middle_name': user.middle_name,
                'email': user.email,
                'photo': user.photo,
                'job_title': titles.get_job_title_display,
                'academic_degree': titles.get_academic_degree_display,
                'academic_title': titles.get_academic_title_display,
                'assignment_date': titles_.assignment_date,
            }
        )

    # print(users_titles)
    context: dict = {
        "users": users_titles,
    }

    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


def load_home_view(request):
    return render(request, "load/load_home.html")


@login_required
def load_on_excel(request: WSGIRequest):
    # print(request.user.username)

    header = [
        "Учебный год",
        "Дата изменения",
        "Факультет",
        "Семестр",
        "Форма обучения",
        "Дисциплина",
        "Курс",
        "Поток",
        "Лекции",
        "Лабораторные",
        "Практические",
        "КП КР",
        "РГР",
        "Контрольные",
        "Консультации",
        "Зачеты",
        "Экзамены",
        "ДП",
        "ГЭК",
        "Практика",
        "Аспирантура",
        "Итого",
        "Примечания",
    ]

    load = Load.objects.filter(on_date=1).order_by("load_info__semester", "load_info__form_study")
    data = load.values(
        # get_verbose_years("load_info__academic_year"),
        "load_info__academic_year",
        "on_date__on_date",
        "load_info__faculty",
        "load_info__semester",
        "load_info__form_study",
        "load_info__discipline__name",
        "load_info__course_study",
        "load_info__group__name",
        "lectures",
        "laboratory",
        "practical",
        "course_work",
        "calculation_and_graphic_works",
        "control",
        "consultations",
        "tests",
        "exams",
        "diploma",
        "state_exam",
        "practice",
        "postgraduate_studies",
        "total",
        "note",
    )
    # data = user.values()
    # print(data)
    data = pd.DataFrame(
        data,
        # columns=[
        #     "Учебный год",
        #     "Дата изменения",
        #     "Факультет",
        #     "Семестр",
        #     "Форма обучения",
        #     "Дисциплина",
        #     "Курс",
        #     "Поток",
        #     "Лекции",
        #     "Лабораторные",
        #     "Практические",
        #     "КП КР",
        #     "РГР",
        #     "Контрольные",
        #     "Консультации",
        #     "Зачеты",
        #     "Экзамены",
        #     "ДП",
        #     "ГЭК",
        #     "Практика",
        #     "Аспирантура",
        #     "Итого",
        #     "Примечания",
        # ]
    )

    # data.append(header, ignore_index=True)
    print(data)
    data.to_excel('d:/data1.xlsx', index=False)
    return render(request, "load/load_home.html")


@login_required
def export_on_excel(request: WSGIRequest):
    # print(request.user.username)
    user = User.objects.filter(username=request.user.username)
    data = user.values("username", "last_name", "first_name", "middle_name")
    # data = user.values()
    # print(data)
    data = pd.DataFrame(data)
    # print(data)
    data.to_excel('d:/data1.xlsx', index=False)
    return render(request, "load/load_home.html")

    # create_data_for_excel(request)
    # file_path = 'data.xlsx'
    # file_name = os.path.basename(file_path)

    # try:
    #     with open(file_path, 'rb') as file:
    #         response = HttpResponse(file, content_type='application/vnd.ms-excel')
    #         response['Content-Disposition'] = 'attachment; filename=' + file_name
    #         os.remove(file_path)  # Удаляем файл после отправки
    #         return response
    # except FileNotFoundError:
    #     return HttpResponse("Файл не найден", status=404)


# def create_data_for_excel(request: WSGIRequest):
#     data = {}
#     user = (User.objects.filter(username=request.user.username)
#             # .select_related("user")
#             # .prefetch_related("load_info")
#             )
#
#     # data = list(user.values("load_info__id", "load__lectures", "load__laboratory", "load__practical"))
#     data = user.values("username", "last_name", "first_name", "middle_name")
#     print(data)
#     # data = list(user.values("username", "last_name", "first_name", "middle_name"))
#     data = pd.DataFrame(data)
#     print(data)
#     # data.to_excel('d:/data1.xlsx', index=False)
#     # df['date'] = df['date'].dt.tz_localize(None)
#     # df.to_excel('data.xlsx', index=False)


def get_verbose_years(years: str) -> str:
    return {
        '23/24': '2023/2024',
        '24/25': '2024/2025',
        '25/26': '2025/2026',
        '26/27': '2026/2027',
        '27/28': '2027/2028',
        '28/29': '2028/2029',
        '29/30': '2029/2030',
    }[years]
