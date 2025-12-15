from django.urls import path
from .views import PostList, PostforDetail

urlpatterns = [path('', PostList.as_view()),
               path('<int:pk>/', PostforDetail.as_view()),
               ]