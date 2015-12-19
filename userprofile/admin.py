from django.contrib import admin
from .models import UserProfile, Status, Friendship, Poke


admin.site.register(UserProfile)
admin.site.register(Status)
admin.site.register(Friendship)
admin.site.register(Poke)
