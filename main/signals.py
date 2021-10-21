from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from main.models import Review

#Create a unique slug for each review so that they can be pulled w/ api
@receiver(pre_save, sender=Review)
def add_slug_to_review(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = get_random_string(length=8)
        instance.slug = slug + '-' + random_string
        