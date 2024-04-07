from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.conf import settings

from load.models import Load
from .models import User, Titles
from .forms import RegisterForm

import os


def register_view(request: WSGIRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
            )
            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request: WSGIRequest):
    user = get_object_or_404(User, username=request.user.username)
    # print(user, user.username, request.user, request.user.username)
    if user != request.user:
        return HttpResponseForbidden("У Вас нет разрешения на редактирование объекта")
    print(user.id)
    titles = Titles.objects.filter(user=user.id).order_by("-assignment_date").first()
    print(titles.assignment_date, titles.academic_title, titles.academic_degree, titles.job_title)
    return render(request, 'user/profile_view.html', {'titles': titles})


@login_required
def profile_update(request: WSGIRequest):
    print(request.user, request.user.username)
    user = get_object_or_404(User, username=request.user.username)
    print(user, user.username, request.user, request.user.username)
    if user != request.user:
        return HttpResponseForbidden("У Вас нет разрешения на редактирование объекта")
    print('ok-li-', request.method)

    if request.method == "POST":
        print('ok-li')

        user = User.objects.get(username=user.username)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.first_name = request.POST.get("first_name", user.first_name)
        user.middle_name = request.POST.get("middle_name", user.middle_name)
        user.phone = request.POST.get("phone", user.phone)
        user.address = request.POST.get("address", user.address)
        user.birthday = request.POST.get("birthday", user.birthday)
        user.description = request.POST.get("description", user.description)
        # user.photo = request.POST.get("photo", user.photo)
        new_photo = request.FILES.get("photoImage")
        if new_photo:
            # Удаление старого изображения
            if user.photo:
                old_photo_path = os.path.join(settings.MEDIA_ROOT, user.photo.name)
                if os.path.isfile(old_photo_path):
                    os.remove(old_photo_path)
            user.photo = new_photo
        user.save()
        print('ok-li')
        # return HttpResponseRedirect(reverse("profile_ok"))
        # return HttpResponseRedirect(reverse("profile_view"))
        # return render(request, 'user/profile_view.html')
        return render(request, "user/update_ok.html", {"user": user})

    return render(request, 'user/profile_update.html')


@login_required()
def titles_history(request: WSGIRequest):
    user = get_object_or_404(User, username=request.user.username)
    titles = Titles.objects.filter(user=user.id).order_by("assignment_date")
    print(titles)
    return render(request, 'user/titles_history.html', {"titles": titles})


@login_required
def titles_update(request: WSGIRequest):
    user = get_object_or_404(User, username=request.user.username)
    titles = Titles.objects.filter(user=user.id).order_by("-assignment_date").first()

    if user != request.user:
        return HttpResponseForbidden("У Вас нет разрешения на редактирование объекта")

    if request.method == "POST":

        user = User.objects.get(username=user.username)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.first_name = request.POST.get("first_name", user.first_name)
        user.middle_name = request.POST.get("middle_name", user.middle_name)
        user.phone = request.POST.get("phone", user.phone)
        user.address = request.POST.get("address", user.address)
        user.birthday = request.POST.get("birthday", user.birthday)
        user.description = request.POST.get("description", user.description)
        # user.photo = request.POST.get("photo", user.photo)
        new_photo = request.FILES.get("photoImage")
        if new_photo:
            # Удаление старого изображения
            if user.photo:
                old_photo_path = os.path.join(settings.MEDIA_ROOT, user.photo.name)
                if os.path.isfile(old_photo_path):
                    os.remove(old_photo_path)
            user.photo = new_photo
        user.save()
        return render(request, "user/update_ok.html", {"user": user})

    return render(request, 'user/titles_update.html', {'titles': titles})


@login_required
def titles_create(request: WSGIRequest):
    print(request.method)
    if request.method == "POST":
        titles = Titles.objects.create(
            job_title=request.POST["job_title"],
            academic_degree=request.POST["academic_degree"],
            academic_title=request.POST["academic_title"],
            assignment_date=request.POST["assignment_date"],
            user=request.user,
        )
        print(titles)
        return render(request, "user/update_ok.html", {"user": request.user})

    titles = Titles.objects.filter(user=request.user.id).first()
    print(titles.JobTitle.choices[1][1])
    return render(request, 'user/titles_create.html', {"titles": titles})


def about_profile(request):
    return render(request, "user/profile_ok.html")


# test
# def load_view(request: WSGIRequest):
#     form = RegisterForm()
#
#     if request.method == 'POST':
#         # load form
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             lectures = form.cleaned_data['lectures']
#             practical = form.cleaned_data['practical']
#             total = lectures + practical
#             Load.objects.create(
#                 lectures=lectures,
#                 practical=practical,
#                 total=total
#             )
#
#             # for update PUT method
#             load = Load.objects.get(id=load_id)
#             load.lectures = lectures
#             load.save(update_field=['lectures'])
#
#             return HttpResponseRedirect(reverse("login"))
#
#     return render(request, 'registration/register-form.html', {'form': form})
