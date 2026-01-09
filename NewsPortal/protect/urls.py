from django.urls import path
from .views import ProtectView

urlpatterns = [
    path('', ProtectView.as_view()),
]