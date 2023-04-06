from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea

from ads.models import Post, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    article = forms.CharField(max_length=255, label='Заголовок:')
    post_text = forms.CharField(label='Текст', widget=TinyMCE(attrs={"cols": 80, "rows": 30}))
    #category = forms.ChoiceField(queryset=Category.objects.all())
    #print(category)


    class Meta:
        model = Post
        fields = [
           'category',
           'article',
           'post_text',
           'slug',
        ]

    def clean_post_text(self):
        post_text = self.cleaned_data["post_text"]
        if post_text is not None and len(post_text) < 20:
            raise ValidationError("Текст не может быть менее 20 символов.")

        return post_text

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=255, label='Текст', widget=Textarea(attrs={"cols": 80, "rows": 10}))

    class Meta:
        model = Comment
        fields = [
           'text',
        ]