from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user', 'message', 'response', 'created_at']
        
class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'message']

class ChatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'