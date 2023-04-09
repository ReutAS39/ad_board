from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Comment, Post


class CommentFilter(FilterSet):
    time_in = DateFilter(lookup_expr='gt', widget=DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('kwarg_I_want_to_pass', None)
        super(CommentFilter, self).__init__(*args, **kwargs)
        #self.queryset = Comment.objects.filter(user_id=self.user)
        self.queryset = Comment.objects.filter(post_id__user_id=self.user)
        self.filters['post'].queryset = Post.objects.filter(user=self.user)
        self.filters['post'].label = "Обьявление"
        self.filters['time_in'].label = "Комментарий создан после"

    class Meta:
        model = Comment
        fields = {
           'post': ['exact'],
                  }

