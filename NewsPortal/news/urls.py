from django.urls import path
from .views import (PostList, PostforDetail, PostSerchList, CreateNews,
                    CreateArticle, UpdateArticle, UpdateNews,DeleteArticle, DeleteNews)

urlpatterns = [path('', PostList.as_view(), name='post-list'),
               path('<int:pk>/', PostforDetail.as_view(), name='post-detail'),
               path('search', PostSerchList.as_view(), name='post-search'),
               path('news_create', CreateNews.as_view(), name='news-create'),
               path('article_create', CreateArticle.as_view(), name='article-create'),
               path('article_edit/<int:pk>', UpdateArticle.as_view(), name='article-edit'),
               path('news_edit/<int:pk>', UpdateNews.as_view(), name='news-edit'),
               path('article_delete/<int:pk>', DeleteArticle.as_view(), name='article-delete'),
               path('news_delete/<int:pk>', DeleteNews.as_view(), name='news-delete'),
               ]