from django.db.models import Count

from ads.models import *

menu = [
        {'title': "Добавить статью", 'url_name': 'post_create'},
        {'title': "Страница пользователя", 'url_name': 'user_page'},
]


class DataMixin:
        paginate_by = 3
        def get_user_context(self, **kwargs):
                context = kwargs
                categories = Category.objects.annotate(Count('post'))
                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.clear()

                context['menu'] = user_menu
                context['categories'] = categories
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context
