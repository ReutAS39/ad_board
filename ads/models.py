from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

POSITION = (
    ('TA', 'Tank'),
    ('HE', 'Heal'),
    ('DD', 'DamageDealer'),
    ('ME', 'Merchant'),
    ('GM', 'GuildMaster'),
    ('QG', 'QuestGiver'),
    ('BS', 'BlackSmith'),
    ('SK', 'Skinner'),
    ('PM', 'PotionMaster'),
    ('SM', 'SpellMaster'),
)


class Category(models.Model):
    name = models.CharField(max_length=255, choices=POSITION)
    slug = models.SlugField('url')

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.CharField(max_length=255)
    post_text = HTMLField()

    def __str__(self):
        return self.article


# class PostCategory(models.Model):
#     # Промежуточная модель для связи «многие ко многим»:
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
