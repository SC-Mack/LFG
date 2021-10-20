from django.db import models

from django.conf import settings
from LFG.core.models import TimeStampModel


class Review(TimeStampModel):
    score = models.IntegerField(verbose_name='User Rating')
    content = models.CharField(max_length=240, verbose_name='User Review Description', blank=True, null=True)
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review')
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.content
