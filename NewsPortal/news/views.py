from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, CategoryAuthor, Category
from .filters import PostFilter
from .forms import NewsForm
from pprint import pprint
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse



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

    def get(self, request, *args, **kwargs):
        hello.delay()
        return HttpResponse("Hello, world. You're at the post list.")

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

class CreateNews(PermissionRequiredMixin,CreateView):
    permission_required = 'news.add_post'
    model = Post
    template_name = 'news_create.html'
    form_class = NewsForm

class CreateArticle(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    model = Post
    template_name = 'article_create.html'
    form_class = NewsForm

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'article_create' in self.request.path:
            post.post_type = 'stat'
            return super().form_valid(form)

class UpdateArticle(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    form_class = NewsForm
    template_name = 'article_edit.html'
    model = Post

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post-search')

class UpdateNews(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        form.save(commit=False)
        send_mail(subject=form.cleaned_data['post_title'],
                  from_email='udalov9494@mail.ru',
                  message=f"{form.cleaned_data['author']} изменил статью {form.cleaned_data['post_title']}",
                  recipient_list=['udalov9494@yandex.ru'], )
        return super().form_valid(form)

class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post-search')

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'caregories.html'
    pprint(context_object_name)



@login_required
def subscribe(request, pk):
    user = request.user
    category = get_object_or_404(Category, id=pk)

    # Проверяем, нет ли уже такой подписки, и создаем её через промежуточную модель
    CategoryAuthor.objects.get_or_create(
        category_author=category,
        author_category=request.user
    )

    return redirect('/news/categories')