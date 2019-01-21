from django.contrib import admin

# Register your models here.

from .models import CustomMessage, InMessage, OutMessage

admin.site.register(CustomMessage)
admin.site.register(InMessage)
admin.site.register(OutMessage)
