from django.urls import path
from django.views.generic import RedirectView

from .views import DetailBlog, NewBlog, UpdateBlog

urlpatterns = [
    path("", RedirectView.as_view(url="blog/new")),
    path("blog", RedirectView.as_view(url="blog/new")),
    path("blog/new", NewBlog.as_view(), name="blog-new"),
    path("blog/<str:title>", DetailBlog.as_view(), name="blog-detail"),
    path("blog/update/<str:title>", UpdateBlog.as_view(), name="blog-update"),
]
