from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pprint import pprint
# Create your views here.
class ProtectView(LoginRequiredMixin, TemplateView):
    template_name = 'protect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        pprint(self.request.user.groups.all())
        return context