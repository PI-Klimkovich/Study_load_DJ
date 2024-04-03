from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest

from load.models import Load
from .models import User
from .forms import RegisterForm


def register_view(request: WSGIRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register-form.html', {'form': form})


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
