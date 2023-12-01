from django.contrib import admin
from .user_data.models import Message, Group, Friend, Good
from .play_data import *

admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)