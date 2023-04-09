from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from ad_board import settings

from ads.models import Comment, Post


@receiver(post_save, sender=Comment)
def email_notify(sender, instance, created, **kwargs):
    if created:
        author_email = []
        author_email.append(User.objects.get(id=Post.objects.get(id=instance.post_id).user_id).email)
        post_article = Post.objects.get(id=instance.post_id).article



        html_content = render_to_string(
                        'email_notify.html',
                        {
                            'instance': instance,
                            'comment_author': User.objects.get(id=instance.user_id).username,
                            #'link': f'{settings.SITE_URL}/news/{instance.id}',
                        })

        send_mail(
                    subject=f'Новый комментарий к твоей статье "{post_article[:50]}"',
                    message=f'Здравствуй Новый комментарий {instance.text[:200]}',
                    from_email='CamcoHKappacko@yandex.ru',
                    recipient_list=author_email,
                    html_message=html_content
                )

    else:
        comment_author_email = []
        comment_author_email.append(User.objects.get(id=instance.user_id).email)
        #post_article = Post.objects.get(id=instance.post_id).article


        html_content = render_to_string(
                        'email_comment_notify.html',
                        {
                            'instance': instance,
                            #'link': f'{settings.SITE_URL}/news/{instance.id}',
                        })

        send_mail(
                    subject=f'Комментарий опубликован ',
                    message=f'Здравствуй Новый комментарий',
                    from_email='CamcoHKappacko@yandex.ru',
                    recipient_list=comment_author_email,
                    html_message=html_content
                )
