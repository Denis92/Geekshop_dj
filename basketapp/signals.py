from django.dispatch import receiver
from django.db.models import signals
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import OrderUser, Basket


@receiver(signals.post_save, sender=OrderUser)
def send_email_ord(instance: OrderUser, created=False, **kwargs):
    if created:
        print('Email_send')
        send_mail('Заказ', 'Поздравляем Вы успешно оформили заказ', f'Admin', ['Denis@mail.ru'])
