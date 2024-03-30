from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from groq import Groq
from django.utils import timezone

grok_api_key = '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'

def ask_groq(message):
    client = Groq(
        api_key = grok_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="mixtral-8x7b-32768",
    )

    answer = chat_completion.choices[0].message.content

    return answer


def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_groq(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message' : message ,'response' : response})
    return render(request, 'grokapp/chat.html', {'chats' : chats})


def test(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_groq(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message' : message ,'response' : response})
    return render(request, 'grokapp/test.html', {'chats' : chats})

# Create your views here.
def app(request):
    return render(request, 'grokapp/home.html')

# def createRoom(request):
#     room = Room.objects.create() 
#     return redirect('room_detail', room_id=room.id)

# def room_detail(request, room_id):
#     room = Room.objects.get(id=room_id)
#     return render(request, 'grokapp/room.html', {'room': room})


# def room(request,pk):
#     chats = Chat.objects.filter(user=request.user)
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = ask_groq(message)

#         chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
#         chat.room = room
#         chat.save()
#         return JsonResponse({'message' : message ,'response' : response})
#     return render(request, 'grokapp/room.html', {'chats' : chats})


