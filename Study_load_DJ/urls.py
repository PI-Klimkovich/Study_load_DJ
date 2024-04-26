"""
URL configuration for Study_load_DJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from load.views import home_page_view, about_view
from django.conf.urls.static import serve
from django.conf import settings
from django.views.decorators.cache import cache_page

# from load.views import filter_notes_view
from user import views

api_v1 = [
    path('', include(('api.users.urls', 'users'), namespace='users')),
    path('', include(('api.notice.urls', 'notice'), namespace='notice')),
    path('', include(('api.load.urls', 'load'), namespace='load')),
    path('', include(('api.distribution.urls', 'distribution'), namespace='distribution')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),

    path('', cache_page(60 * 15)(home_page_view), name='home'),
    path('about', cache_page(60 * 15)(about_view), name='about'),
    # path("filter", filter_notes_view, name="filter-notes"),

    path('user/', include("user.urls")),
    path('load/', include("load.urls")),
    path('notice/', include("notice.urls")),
    path('distribution/', include("distribution.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # path("__debug__/", include("debug_toolbar.urls")),

    path('api/v1/', (api_v1, 'api', 'api')),
]
