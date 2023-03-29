from django.db import models
from tinymce.models import HTMLField

POSITION = (
    ('PO', 'Article'),
    ('NE', 'News')
)

class Category(models.Model):
    # Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
    name = models.CharField(max_length=255, choices=POSITION)  # название категории. Поле должно быть уникальным
    #subscribers = models.ManyToManyField(User)

class Post(models.Model):
    # Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    # Каждый объект может иметь одну или несколько категорий.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Author;
    time_in = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    category = models.ManyToManyField(Category, through='PostCategory')
    article = models.CharField(max_length=255)  # заголовок статьи/новости;
    post_text = HTMLField()


class PostCategory(models.Model):
    # Промежуточная модель для связи «многие ко многим»:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Category.


class Comment(models.Model):
    # Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# (комментарии может оставить любой пользователь, необязательно автор);
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)

