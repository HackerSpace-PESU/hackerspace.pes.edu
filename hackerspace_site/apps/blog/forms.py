from django.forms import ModelChoiceField, ModelForm
from martor.fields import MartorFormField

from .models import Author, Blog


class NewBlogForm(ModelForm):
    author = ModelChoiceField(
        queryset=Author.objects.all(),
    )
    blog_in_markdown = MartorFormField()

    class Meta:
        model = Blog
        fields = ["author", "title", "blog_in_markdown"]
