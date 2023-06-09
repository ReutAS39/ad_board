# Generated by Django 4.1.7 on 2023-04-08 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Tank', 'Tank'), ('Healer', 'Heal'), ('DamageDealer', 'DamageDealer'), ('Merchant', 'Merchant'), ('Guildmaster', 'GuildMaster'), ('QuestGiver', 'QuestGiver'), ('Blacksmith', 'BlackSmith'), ('Skinner', 'Skinner'), ('PotionMaster', 'PotionMaster'), ('SpellMaster', 'SpellMaster')], max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.CharField(max_length=255)),
                ('post_text', tinymce.models.HTMLField(blank=True, default='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='ads.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
