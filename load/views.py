from django.shortcuts import render

# from .models import Load
from user.models import User, Titles


def home_page_view(request):
    all_users = User.objects.all()  # Получение всех записей из таблицы этой модели.
    # all_users = (
    #     User.objects.all()
    #     # .select_related("user.id")  # Вытягивание связанных данных из таблицы User в один запрос
    #     .annotate(
    #         reception_date=Titles.objects.filter(user=user.id).order_by("assignment_date")
    #     )
    # )
    context: dict = {
        "users": all_users[:20],

    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")
