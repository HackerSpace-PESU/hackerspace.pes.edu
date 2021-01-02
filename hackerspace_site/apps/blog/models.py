from django.contrib.auth.models import User
from django.db import models
from martor.models import MartorField


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=128, unique=True)
    blog_in_markdown = MartorField()

    def __str__(self):
        return self.title
