from django.urls import path
from .views import BaseRegisterView, upgrade_me

urlpatterns = [
    path('signup', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]