from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("martor/", include("martor.urls")),
    path("admin/", admin.site.urls),
    path("", include("hackerspace_site.apps.blog.urls")),
]
