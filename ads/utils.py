from ads.models import Category

menu = [
        {'title': "Добавить статью", 'url_name': 'post_create'},
        {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                categories = Category.objects.all()
                context['menu'] = menu
                context['categories'] = categories
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context