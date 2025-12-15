from django.views.generic import ListView, DetailView
from .models import Post
from pprint import pprint

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-post_date'
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenght'] = len(self.context_object_name) - 1
        # pprint(context)
        return context

class PostforDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'