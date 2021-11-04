from django.contrib import admin

from .models import CustomUser, WishGame

admin.site.register(CustomUser)
admin.site.register(WishGame)
