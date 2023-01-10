from django.contrib import admin
from .models import UserModel, MessageModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(MessageModel)
