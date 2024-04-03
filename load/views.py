from django.shortcuts import render

# from .models import Load
from user.models import User


def home_page_view(request):
    all_users = User.objects.all()  # Получение всех записей из таблицы этой модели.
    context: dict = {
        "users": all_users[:20]
    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")
