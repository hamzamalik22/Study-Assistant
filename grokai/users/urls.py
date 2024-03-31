
from django.urls import path
from .views import UserLogin, UserRegister, UserLogout

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user-login'),
    path('Register/', UserRegister.as_view(), name='user-register'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
]
