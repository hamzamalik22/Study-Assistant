from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', ChatAPI.as_view(), name='chat-api'),
    path('history/', ChatListAPI.as_view(), name='chat-list'),
    path('historyDetail/<int:id>/', ChatDetailAPI.as_view(), name='chat-detail'),
]
