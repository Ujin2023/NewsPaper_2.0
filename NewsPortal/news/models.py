from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    author_rat = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        author_posts_rat = 0
        author_comment_rat = 0
        comment_author_rat = 0
        posts = Post.objects.filter(author=self)
        for post in posts:
            author_posts_rat += post.post_rate
        comments = Comment.objects.filter(user_comment=self.user)
        for comment in comments:
            author_comment_rat += comment.comment_rate
        post_comments = Comment.objects.filter(post_comment__author = self)
        for post_comment in post_comments:
            comment_author_rat += post_comment.comment_rate
        self.author_rat = author_posts_rat * 3 + author_comment_rat + comment_author_rat
        self.save()

class Category(models.Model):
    category_theme = models.CharField(max_length = 30, unique = True)
    subscribers = models.ManyToManyField(User, through = 'CategoryAuthor', related_name='categories')

    def __str__(self):
        return self.category_theme

class Post(models.Model):
    stat = "stat"
    news = "news"
    CHOICE = [(stat, "Статья"),
              (news, "Новости")]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length = 10, choices = CHOICE, default = news)
    post_category = models.ManyToManyField(Category, through = "PostCategory")
    post_title = models.CharField(max_length = 50)
    post_rate = models.IntegerField(default = 0)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add = True)

    def like(self):
        self.post_rate += 1
        self.save()
    def dislike(self):
        self.post_rate -= 1
        self.save()
    def preview(self):
        return self.post_text[:124] + "..."
    def __str__(self):
        return self.post_text
    def get_absolute_url(self):
        return reverse('post-search')


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete = models.CASCADE)
    category_post = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add = True)
    comment_rate = models.IntegerField(default = 0)
    comment_text = models.TextField()
    user_comment = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.comment_rate += 1
        self.save()
    def dislike(self):
        self.comment_rate -= 1
        self.save()

class CategoryAuthor(models.Model):
    category_author = models.ForeignKey(Category, on_delete = models.CASCADE)
    author_category = models.ForeignKey(User, on_delete = models.CASCADE)

