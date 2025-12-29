from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import NewsForm
from pprint import pprint
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-post_date'
    template_name = 'posts.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenght'] = len(self.context_object_name)
        return context

class PostforDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'

class PostSerchList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'search.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        context['lenght'] = len(self.context_object_name)
        return context

class CreateNews(CreateView):
    model = Post
    template_name = 'news_create.html'
    form_class = NewsForm

class CreateArticle(CreateView):
    model = Post
    template_name = 'article_create.html'
    form_class = NewsForm

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'article_create' in self.request.path:
            post.post_type = 'stat'
            return super().form_valid(form)

class UpdateArticle(UpdateView):
    form_class = NewsForm
    template_name = 'article_edit.html'
    model = Post

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post-search')

class UpdateNews(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post-search')