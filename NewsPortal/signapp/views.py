from django.shortcuts import render, redirect
from pprint import pprint
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.decorators import login_required

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/search/'

@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    pprint(author_group)
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/')