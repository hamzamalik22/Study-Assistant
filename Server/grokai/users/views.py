from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return JsonResponse({'error': 'Username or Password Incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

class UserRegister(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)
        

class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'User logged out'})
