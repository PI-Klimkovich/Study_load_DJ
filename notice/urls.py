from django.urls import path
from . import views

urlpatterns = [
    path('', views.notices_page_view, name='notices_view'),
    path('create', views.create_notice_view, name='create'),
    path('create_ok', views.about_create, name='create_ok'),
    path('<uuid:notice_uuid>', views.show_notice_view, name='notice'),
    path("<notice_uuid>/update", views.update_notice_view, name="update"),
    path("<notice_uuid>/delete", views.delete_notice_view, name="delete"),
    path("<username>/notices", views.user_notices_view, name="user_notices"),
    path("<username>/u_notices", views.your_notices_view, name="your_notices"),
]
