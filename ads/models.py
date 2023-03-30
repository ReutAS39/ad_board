from django.db import models
from tinymce.models import HTMLField

POSITION = (
    ('PO', 'Article'),
    ('NE', 'News')
)

class Category(models.Model):
    # Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
    name = models.CharField(max_length=255, choices=POSITION)
    #subscribers = models.ManyToManyField(User)
    slug = models.SlugField('url')

class Post(models.Model):
    # Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    # Каждый объект может иметь одну или несколько категорий.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory') #models.ForeignKey
    article = models.CharField(max_length=255)
    post_text = HTMLField()


class PostCategory(models.Model):
    # Промежуточная модель для связи «многие ко многим»:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    # Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# (комментарии может оставить любой пользователь, необязательно автор);
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)

