from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import UserModel, MessageModel
from django.contrib.auth.models import User
from .serializers import MessageSerializer
from rest_framework.views import APIView
import telebot
import os

bot_token = os.getenv('TOKEN')
bot = telebot.TeleBot(bot_token)


class BearerAuthentication(TokenAuthentication):
    keyword = "Bearer"


class RegistrationView(APIView):
    def post(self, request):
        new_user = User.objects.create(username=request.data["username"])
        token = Token.objects.create(user=new_user)

        UserModel.objects.create(
            user=new_user,
            token=token,
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            chat_id='-',
        )
        return Response(f"Your token is {token.key}")


class MessageView(APIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = MessageModel.objects.filter(
            user=UserModel.objects.get(user=request.user)
        )
        return Response(MessageSerializer(queryset, many=True).data)

    def post(self, request):
        message = request.data["message"]
        user_instance = UserModel.objects.get(user=request.user)
        chat_id = user_instance.chat_id
        if chat_id == '-':
            return Response("Please link the token to the chat")

        MessageModel.objects.create(user=user_instance, message=message)
        bot.send_message(chat_id, message)
        return Response("Message has been sent")
