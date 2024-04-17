from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .bot import telegram_bot_send

from .models import Notice
from user.models import User


def notices_page_view(request):
    all_notices = (Notice.objects.all()
                   .select_related("user")  # Вытягивание связанных данных из таблицы User в один запрос
                   .order_by("-created_at")  # Сортировка результатов по убыванию по created_at
                   )

    context: dict = {
        "notices": all_notices[:20]
    }
    return render(request, "notice/notices_view.html", context)


def about_create(request):
    return render(request, "notice/create_ok.html")


@login_required
def create_notice_view(request: WSGIRequest):
    if request.method == "POST":
        notice = Notice.objects.create(
            message=request.POST["message"],
            user=request.user,
        )
        post = (f"{notice.message}\n"
                f"    {request.user.last_name} {request.user.first_name[0]}.{request.user.middle_name[0]}."
                )
        response = telegram_bot_send(post)
        # print(response)

        return render(request, "notice/create_ok.html", {"notice": notice})

    # Вернется только, если метод не POST.
    return render(request, "notice/create_notice.html")


def show_notice_view(request: WSGIRequest, notice_uuid):
    try:
        notice = Notice.objects.get(uuid=notice_uuid)  #
    except Notice.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404

    return render(request, "notice/notice.html", {"notice": notice})


@login_required
def delete_notice_view(request: WSGIRequest, notice_uuid: str):
    notice = get_object_or_404(Notice, uuid=notice_uuid)
    if notice.user != request.user:
        return HttpResponseForbidden("У Вас нет разрешения на удаление объекта")

    if request.method == "POST":
        Notice.objects.get(uuid=notice_uuid).delete()
    return HttpResponseRedirect(reverse("notices_view"))


@login_required
def update_notice_view(request: WSGIRequest, notice_uuid):
    notice = get_object_or_404(Notice, uuid=notice_uuid)
    if notice.user != request.user:
        return HttpResponseForbidden("У Вас нет разрешения на редактирование объекта")

    if request.method == "POST":
        notice = Notice.objects.get(uuid=notice_uuid)
        notice.message = request.POST.get('message', notice.message)
        notice.mod_time = timezone.now()
        notice.save()

        post = (f"ИЗМЕНЕНО\n"
                f"{notice.message}\n"
                f"    {request.user.last_name} {request.user.first_name[0]}.{request.user.middle_name[0]}."
                )
        response = telegram_bot_send(post)
        # print(response)

        return render(request, "notice/update_ok.html", {"notice": notice})

    notice = Notice.objects.get(uuid=notice_uuid)
    return render(request, "notice/update_notice.html", {"notice": notice})


# заметки выбранного пользователя
def user_notices_view(request: WSGIRequest, username):
    # print(username)
    user = User.objects.get(username=username)
    # print(user)
    user_notices = Notice.objects.filter(user=user).order_by("-created_at")
    return render(request, 'notice/user_notices.html', {"notices": user_notices, "username": user})


# заметки авторизованного пользователя
@login_required()
def your_notices_view(request: WSGIRequest, username):
    user = User.objects.get(username=username)
    user_notices = Notice.objects.filter(user=user).order_by("-created_at")
    return render(request, 'notice/your_notices.html', {"notices": user_notices, "username": user})
