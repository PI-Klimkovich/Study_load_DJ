from django.shortcuts import render

# from .models import Load
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
