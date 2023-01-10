from requests.exceptions import ConnectionError, ReadTimeout
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from app.models import UserModel
from app.views import bot
import sys
import os


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Please send the token')
    else:
        try:
            token = Token.objects.get(key=message.text)
            user_instance = UserModel.objects.get(user=token.user)
            print(user_instance)
            user_instance.chat_id = message.chat.id
            user_instance.save()
            bot.send_message(message.chat.id, 'Token has been registered')
        except:
            bot.send_message(message.chat.id, 'Incorrect token')


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except (ConnectionError, ReadTimeout):
            sys.stdout.flush()
            os.execv(sys.argv[0], sys.argv)
        else:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
