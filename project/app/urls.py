from django.urls import path
from .views import RegistrationView, MessageView


urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('messages/', MessageView.as_view()),
]
