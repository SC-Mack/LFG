from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    
    # avatar = models.ImageField()
    intro = models.CharField(max_length=140, verbose_name='Intro Line', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    current_game = models.CharField(max_length=100, blank=True, null=True)
    play_style = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Review(models.Model):
    comment = models.CharField(max_length=240, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)


class Conversation(models.Model):
    message = models.CharField(max_length=300, blank=True, null=True)
