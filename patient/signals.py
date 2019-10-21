from django.db.models.signals import post_save
from django.dispatch import receiver
from patient.models import *

@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = PatientProfile(user=user)
        profile.save()
