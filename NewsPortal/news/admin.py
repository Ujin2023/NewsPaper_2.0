from django.contrib import admin
from .models import Post, PostCategory, CategoryAuthor


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(CategoryAuthor)
