from django.shortcuts import render

# def index(request):
#     return render(request, 'indextmp.html')
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Post

menu = [#{'title': "О сайте", 'url_name': 'about'},
        #{'title': "Добавить статью", 'url_name': 'ads_create'},
        #{'title': "Обратная связь", 'url_name': 'contact'},
        #{'title': "Войти", 'url_name': 'login'}
]

class AdsList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'ads'
    #paginate_by = 10  # вот так мы можем указать количество записей на странице


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return self.queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['news_count'] = f'Количество статей: {self.filterset.qs.count()}'
        # # чтобы на её примере рассмотреть работу ещё одного фильтра.
        # # Добавляем в контекст объект фильтрации.
        # context['filterset'] = self.filterset
        # # Добавим ещё одну пустую переменную,
        # # чтобы на её примере рассмотреть работу ещё одного фильтра.
        # context['next_sale'] = None
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        context['menu'] = menu
        # context['is_author'] = self.request.user.groups.filter(name='authors').exists()

        return context

class AdsDetail(DetailView):
    pass

class AdsCreate(CreateView):
    pass

class AdsUpdate(UpdateView):
    pass

class AdsDelete(DeleteView):
    pass