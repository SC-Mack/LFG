from django.contrib import admin

from .models import CustomUser, OwnedGame, WishGame

admin.site.register(CustomUser)
admin.site.register(OwnedGame)
admin.site.register(WishGame)
