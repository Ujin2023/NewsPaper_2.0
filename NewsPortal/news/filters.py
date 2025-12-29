from django_filters import FilterSet, ModelChoiceFilter, TimeFilter, CharFilter, DateTimeFilter
from .models import Post, Author, User
from django import forms


class PostFilter(FilterSet):
    author = ModelChoiceFilter(field_name="author__user", queryset=User.objects.filter(pk__in =Author.objects.all() ),
                               label= "Автор:", empty_label='по всем авторам')
    post_date = DateTimeFilter(lookup_expr='gte', label= "Дата с:", widget=forms.DateInput(attrs={'type': 'date'}))
    post_title = CharFilter( lookup_expr='icontains', label= "Заголовок содержит:")

    class Meta:
        model = Post
        fields = ['author',
                  'post_date',
                  'post_title']