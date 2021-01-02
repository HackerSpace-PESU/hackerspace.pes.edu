from django.forms import ModelForm
from martor.fields import MartorFormField

from .models import Blog


class NewBlogForm(ModelForm):
    blog_in_markdown = MartorFormField()

    class Meta:
        model = Blog
        fields = ["title", "blog_in_markdown"]
