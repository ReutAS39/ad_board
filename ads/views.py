import os
from uuid import uuid4

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import resolve, reverse_lazy
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from ads.filters import CommentFilter
from ads.forms import PostForm, CommentForm
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


class UserPage(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'user_page.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, kwarg_I_want_to_pass=self.request.user.id, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Страница пользователя'
        context['filterset'] = self.filterset
        return context

def edit_comment_status(request, pk, type):
    c = Comment.objects.get(pk=pk)
    if type == 'public':
        c.status = True
        c.save()


class PostDetail(DataMixin, DetailView, FormMixin):
    model = Post
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"{context['post'].article}")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Комментарий добавлен.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Редактирование статьи'
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f"Удаление статьи {context['post'].article}"
        return context


@csrf_exempt
def upload_image(request, category, post):
    if request.method != 'POST':
        return JsonResponse({"Error Message": "Wrong request"})

    matching_article = Post.objects.filter(category__slug=category, post_slug=post).first()
    if not matching_article:
        return JsonResponse({"Error Message": f"Wrong series({category}) or article ({post})"})

    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split('.')[-1]
    if file_name_suffix not in ['jpg', 'png', 'gif', 'jpeg']:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .git, .jpeg"})

    file_path = os.path.join(settings.MEDIA_ROOT, 'Category', matching_article.slug, file_obj.name)

    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(settings.MEDIA_ROOT, 'Category', matching_article.slug, file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    return JsonResponse({
        "Message": "Image upload successfully",
        "location": os.path.join(settings.MEDIA_URL, 'Category', matching_article.slug, file_obj.name)
        })
