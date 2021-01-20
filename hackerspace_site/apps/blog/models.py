from django.contrib.auth.models import User
from django.db import models
from martor.models import MartorField


class Author(models.Model):
    name = models.CharField(max_length=256, unique=True)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=128, unique=True)
    blog_in_markdown = MartorField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]
