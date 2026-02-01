from django.urls import path
from .views import ProtectView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(ProtectView.as_view())),
]