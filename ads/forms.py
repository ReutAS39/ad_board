from django import forms
from django.core.exceptions import ValidationError

from ads.models import Post, POSITION, Category


class PostForm(forms.ModelForm):
    article = forms.CharField(max_length=255, label='Заголовок:')
    #category = forms.ChoiceField(queryset=Category.objects.all())
    #print(category)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].empty_label = 'Выберите автора'
        # self.fields['position'].initial = 'NE'

    class Meta:
        model = Post
        fields = [
           'user',
           'category',
           'article',
           'post_text',
           'slug',
        ]
        # widgets = {
        #    'article': forms.TextInput(attrs={'class': 'form-input'}),
        #    'text': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        # }

        labels = {
           'post_text': 'Текст',
           'user': 'Автор:',
           'category': 'Категория:',
           'position': 'Статья/Новость:',
        }

    def clean_post_text(self):
        post_text = self.cleaned_data["post_text"]
        if post_text is not None and len(post_text) < 20:
            raise ValidationError("Текст не может быть менее 20 символов.")

        return post_text
