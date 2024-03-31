from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [ 'user', 'message', 'response', 'created_at']
