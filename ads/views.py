from django.urls import resolve
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Post, Category

menu = [#{'title': "О сайте", 'url_name': 'about'},
        #{'title': "Добавить статью", 'url_name': 'ads_create'},
        #{'title': "Обратная связь", 'url_name': 'contact'},
        #{'title': "Войти", 'url_name': 'login'}
]


class PostList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'
    #paginate_by = 10  # вот так мы можем указать количество записей на странице

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        # context['is_author'] = self.request.user.groups.filter(name='authors').exists()

        return context


class CategoryList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        # self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # queryset = super().get_queryset()
        # self.filterset = PostFilter(self.request.GET, queryset.filter(category=self.kwargs['pk']))
        # return self.filterset.qs
        return Post.objects.filter(cat__id=self.kwargs['cat_id'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category_get = Category.objects.get(pk=resolve(self.request.path_info).kwargs['pk'])
    #     # # context['filterset'] = self.filterset
    #     # # context['title'] = 'Категория - ' + str(category_get)
    #     # # context['menu'] = menu
    #     # # context['cat_selected'] = context['news_list'][0].category.get()
    #     # context['cat_selected'] = category_get
    #     # context['news_count'] = f'Количество статей в категории {category_get}: {self.filterset.qs.count()}'
    #     # context['cat_subscriber'] = Category.objects.filter(subscribers__pk=self.request.user.id)
    #     # context['is_author'] = self.request.user.groups.filter(name='authors').exists()
    #
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = f"{context['news'].article}"
        # context['cat_subscriber'] = Category.objects.filter(subscribers__pk=self.request.user.id)
        # context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        # context['cat_selected'] = context['news'].category.get()

        return context


class PostCreate(CreateView):
    pass


class PostUpdate(UpdateView):
    pass


class PostDelete(DeleteView):
    pass

