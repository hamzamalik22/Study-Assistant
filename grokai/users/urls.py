from django.urls import path
from . import views

urlpatterns = [
    path('loginPage/', views.loginUser, name='login-User'),
    path('RegisterPage/', views.RegisterUser, name='Register-User'),
    path('logoutPage/', views.logoutUser, name='logout-User'),
]
