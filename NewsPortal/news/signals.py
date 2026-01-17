from django.core.mail import send_mail, EmailMessage
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from .models import Post, PostCategory
from pprint import pprint


@receiver(m2m_changed, sender=Post.post_category.through)
def notify(sender, instance, action, **kwargs):
# instance и created - instance хранит в себе только что сохранённый объект модели sender, а created — булева переменная,
# которая хранит в себе True или False в зависимости от того, как вы могли догадаться, есть ли такой объект в базе или нет
        if action == 'post_add':
            categories = instance.post_category.all()
            pprint(categories)
            subscribers_emails = []
            for category in categories:
                subscribers_emails += [s.email for s in category.subscribers.all()]
                subscribers_emails = list(set(subscribers_emails))
                pprint(subscribers_emails)

            subject = f'В вашей любимой категории размещена новая статья {instance.post_title}'
            msg = EmailMessage(
                subject=subject,
                body=instance.post_text,
                to=subscribers_emails,
            )
            msg.send()