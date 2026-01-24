from django.contrib import admin
from .models import Post, PostCategory, CategoryAuthor, Category


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(CategoryAuthor)
admin.site.register(Category)
