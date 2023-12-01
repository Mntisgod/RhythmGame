from django.contrib import admin
from .user_data.models import Message, Group, Friend, Good
from .game_data.models import Player, PlayData, Chart, Song

admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)
admin.site.register(Player)
admin.site.register(Chart)
admin.site.register(Song)