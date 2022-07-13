from django.contrib import admin

from .models import User, Reserved, Notification

admin.site.register(User)
admin.site.register(Reserved)
admin.site.register(Notification)
