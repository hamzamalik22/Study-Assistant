from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated
from django.utils import timezone
import requests

class ChatAPI(APIView):
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission

    def post(self, request):
        message = request.data.get('message')
        if message:
            response = self.ask_groq(message)
            chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
            chat.save()
            serializer = ChatSerializer(chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

    def ask_groq(self, message):
        grok_api_key = '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'
        url = 'https://api.grok.ai/chat/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {grok_api_key}'}
        data = {'message': message}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('response')
        else:
            return 'Error occurred during response'
