from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True, null=True)
    blurb = models.CharField(max_length=150, verbose_name='Short Description', blank=True, null=True)
    bio = models.TextField(verbose_name='Bio', blank=True, null=True)
    rating = models.DecimalField(max_digits=3,decimal_places=1, verbose_name='Rating', null=True, blank=True, editable=False)
    time_zone = models.CharField(max_length=7, blank=True, null=True)
    preferred_genres = models.CharField(max_length=10, verbose_name='Preferred Game Genres', blank=True, null=True) #Will need GB API
    current_games = models.CharField(max_length=100, verbose_name='Current Played Games', blank=True, null=True)#Will need GB API
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
            return self.username
    