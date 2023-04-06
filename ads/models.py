from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

POSITION = (
    ('Tank', 'Tank'),
    ('Healer', 'Heal'),
    ('DamageDealer', 'DamageDealer'),
    ('Merchant', 'Merchant'),
    ('Guildmaster', 'GuildMaster'),
    ('QuestGiver', 'QuestGiver'),
    ('Blacksmith', 'BlackSmith'),
    ('Skinner', 'Skinner'),
    ('PotionMaster', 'PotionMaster'),
    ('SpellMaster', 'SpellMaster'),
)


class Category(models.Model):
    name = models.CharField(max_length=255, choices=POSITION)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.CharField(max_length=255)
    post_text = HTMLField(blank=True, default="")

    def __str__(self):
        return self.article

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
