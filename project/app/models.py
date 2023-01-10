from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    chat_id = models.CharField(max_length=50)


class MessageModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
