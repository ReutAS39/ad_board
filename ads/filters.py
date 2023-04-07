from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Comment


class CommentFilter(FilterSet):
    time_in = DateFilter(lookup_expr='gt', widget=DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))

    class Meta:
        model = Comment
        fields = {

           'post': ['exact'],
          # 'post': ['exact'],
                  }

    def __init__(self, *args, **kwargs):
        super(CommentFilter, self).__init__(*args, **kwargs)
        #self.filters['article__icontains'].label = "Заголовок"  # не меняется
        self.filters['post'].label = "Обьявление"
        self.filters['time_in'].label = "Дата"