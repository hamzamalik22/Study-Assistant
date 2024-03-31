from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer,ChatListSerializer,ChatDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.utils import timezone
import requests
from groq import Groq 
import os

# For Chating
class ChatAPI(APIView):
    permission_classes = [IsAuthenticated]

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
        
        grok_api_key = os.environ.get("GROQ_API_KEY")
        if not grok_api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")

        client = Groq(api_key=grok_api_key)

        # Make the request to Grok API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="mixtral-8x7b-32768",
        )

        return chat_completion.choices[0].message.content


# For history
class ChatListAPI(ListAPIView):
    """
    Endpoint to retrieve a list of chat messages.
    """
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer

# For Detail History
class ChatDetailAPI(RetrieveAPIView):
    """
    Endpoint to retrieve details of a single chat message.
    """
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatDetailSerializer
    lookup_field = 'id'