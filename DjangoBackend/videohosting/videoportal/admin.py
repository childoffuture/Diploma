from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(Subscription)
admin.site.register(Chat)
admin.site.register(ChatMessage)
