from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import resolve, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.forms import PostForm
from ads.models import Post
from ads.utils import *


class PostList(DataMixin, ListView):
    model = Post
    ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class CategoryList(DataMixin, ListView):
    model = Post
    # ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self, **kwargs):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].category),
                                      cat_selected=context['posts'][0].category_id)
        return dict(list(context.items()) + list(c_def.items()))


class PostDetail(DataMixin, DetailView):
    model = Post
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"{context['post'].article}")
        return dict(list(context.items()) + list(c_def.items()))


class PostCreate(LoginRequiredMixin, DataMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    # login_url = reverse_lazy('post_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


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

