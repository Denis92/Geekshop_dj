from django.dispatch import receiver
from django.db.models import signals
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import ShopUser


@receiver(signals.post_save, sender=ShopUser)
def set_book_read(instance: ShopUser, created=False, **kwargs):
    if created:
        print(ShopUser.objects.last().email)
        send_mail('Регистрация', 'Поздравляем Вы успешно прошли регистрацию', f'Admin', [instance.email])