from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    
    HARDCORE = 'Hardcore'
    CASUAL = 'Casual'
    CHOICES = [
        (HARDCORE, 'Hardcore'),
        (CASUAL, 'Casual'),
    ]
    
    # avatar = models.ImageField()
    intro = models.CharField(max_length=140, verbose_name='Intro Line', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    current_game = models.CharField(max_length=100, blank=True, null=True)
    play_style = models.CharField(max_length=50, choices=CHOICES,blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username
    
class WishGame(models.Model):
    wisher = models.ForeignKey(CustomUser, on_delete=CASCADE)
    api_id = models.IntegerField(unique=True)