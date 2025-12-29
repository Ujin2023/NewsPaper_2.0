
from django import forms
from .models import Post

class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author',
                  'post_title',
                  'post_text',
                  'post_category',
                  ]

