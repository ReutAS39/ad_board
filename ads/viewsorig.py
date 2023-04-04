from django.http import HttpResponse
from django.urls import resolve, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.forms import PostForm
from ads.models import Post
from ads.utils import *

menu = [
        {'title': "Добавить статью", 'url_name': 'post_create'},
        {'title': "Войти", 'url_name': 'login'}
]


class PostList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'
    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


class CategoryList(ListView):
    model = Post
    # ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self, **kwargs):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].category_id
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f"{context['post'].article}"
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Создание статьи'
        return context


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Редактирование статьи'
        return context


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f"Удаление статьи {context['post'].article}"
        return context


def login(request):
    return HttpResponse("Авторизация")
