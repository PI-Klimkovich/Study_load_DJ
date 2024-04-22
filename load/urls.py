from django.urls import path
from . import views

urlpatterns = [
    path('home', views.load_home_view, name='load_home'),
    path('export', views.export_on_excel, name="export")
    # path('create', views.create_note_view, name='create'),
    # path('tags', views.show_tags_view, name='all_tags'),
    # path('tag_notes', views.show_tags_view, name='tag_notes'),
    # path('<uuid:note_uuid>', views.show_note_view, name='note'),
    # path("<note_uuid>/update", views.update_note_view, name="update"),
    # path("<note_uuid>/delete", views.delete_note_view, name="delete"),
    # path("<username>/notes", views.user_notes_view, name="user_notes"),
    # path("<username>/u_notes", views.your_notes_view, name="your_notes"),
    # path("<tag>/t_notes", views.tag_notes_view, name="tag_notes"),
    # path("<tag>", views.tag_notes_view, name="tag_notes"),
]
