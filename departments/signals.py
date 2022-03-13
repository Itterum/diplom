from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Department


@receiver(post_save, sender=Department)
def my_callback(sender, **kwargs):
    print("Request finished!")
