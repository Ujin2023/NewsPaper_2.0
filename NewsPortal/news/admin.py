from dataclasses import field

from django.contrib import admin
from .models import Post, PostCategory, CategoryAuthor, Category
from pprint import pprint

def null_text(modeladmin, request, queryset):
    queryset.update(post_text='')
null_text.short_description = 'Обнулить текст статьи'
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['post_type','post_title', 'post_rate', 'post_text', 'post_date', 'post_category__category_theme',]# генерируем список имён всех полей для более красивого отображения
    list_filter = ['post_type', 'post_title', 'post_rate', 'post_text', 'post_date', ]
    search_fields = ['post_type', 'post_title','post_category__category_theme']
    actions = [null_text]
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(CategoryAuthor)
admin.site.register(Category)
