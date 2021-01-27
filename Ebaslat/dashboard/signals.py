from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Store

@receiver(post_save, Sender = User)
def CreateStore(sender, instance, created, **kwargs):
    if created:
        Store.objects.create(user = instance)

@receiver(post_save, Sender = User)
def UpdateStore(sender, instance, created, **kwargs):
    if created == False:
        Store.objects.save()
