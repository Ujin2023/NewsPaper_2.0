from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User
from .models import Post
from pprint import pprint

@shared_task
def send_weekly_newsletter():
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(post_date__gte=last_week)
    if not posts.exists():
        return "Нет новых новостей за неделю"
    users_emails = User.objects.filter(email__isnull=False).exclude(email='')
    emails = [user.email for user in users_emails]
    msg = EmailMultiAlternatives(
        subject='Ваш еженедельный дайджест новостей из CELERY',
        body='Есть новые новости за неделю',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=emails,
    )
    msg.send()
    return f"Рассылка отправлена {len(emails)} пользователям"
