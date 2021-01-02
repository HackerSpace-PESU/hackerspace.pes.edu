from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView

from .forms import NewBlogForm
from .models import Blog


class SuperUserAccessMixin(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.is_superuser

    def handle_no_permission(self) -> None:
        raise Http404()


class NewBlog(SuperUserAccessMixin, View):
    """Blog creation view."""

    template_name = "blog/new_blog.html"

    def get(self, request: WSGIRequest) -> HttpResponse:
        """HTTP GET: Return the view template."""
        context = {"form": NewBlogForm}
        return render(request, self.template_name, context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        """HTTP POST: Process creation of new Blog."""
        blog = NewBlogForm(request.POST)

        if blog.is_valid():
            obj = blog.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect("blog-detail", title=obj.title)

        context = {"form": NewBlogForm}
        return render(request, self.template_name, context)


class DetailBlog(DetailView):
    """Blog detail view, display individual blogs."""

    template_name = "blog/detail_blog.html"
    model = Blog
    slug_field = "title"
    slug_url_kwarg = "title"


class UpdateBlog(SuperUserAccessMixin, View):
    """Blog update view, to make modification to a blog."""

    def get(self, request: WSGIRequest, title: str) -> HttpResponse:
        """HTTP GET: Return the view template."""
        blog = Blog.objects.get(title=title)
        form = NewBlogForm(instance=blog)
        context = {"form": form}
        return render(request, "blog/update.html", context)

    def post(self, request: WSGIRequest, title: str) -> HttpResponse:
        """HTTP POST: Process blog modification."""
        blog = Blog.objects.get(title=title)
        form = NewBlogForm(request.POST, instance=blog)
        if form.is_valid():
            obj = form.save()
            return redirect("blog-detail", title=obj.title)

        context = {"form": form}

        return render(request, "blog/update.html", context)
