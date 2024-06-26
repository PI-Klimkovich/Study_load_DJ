from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page

from . import views

# /user/

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile_ok/', views.about_profile, name='profile_ok'),
    path("profile/", views.profile_view, name="profile-view"),
    path("profile/update", views.profile_update, name="profile-update"),
    path("titles/update", views.titles_update, name="titles-update"),
    path("titles/history", cache_page(60 * 15)(views.titles_history), name="titles-history"),
    path("titles/create", views.titles_create, name="titles-create"),
    path("teachers", cache_page(60 * 15)(views.teachers_view), name="teachers"),
    path("teacher/<username>", views.teacher_view, name="teacher"),
]
