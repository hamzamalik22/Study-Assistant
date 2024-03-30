from django.urls import path
from . import views

urlpatterns = [
    path('',views.app,name='home'),
    path('chat/',views.chatbot,name='chatbot'),
    path('test/',views.test,name='test'),
    # path('room/<str:pk>',views.room,name='room'),
    # path('create_room/', views.createRoom, name='create_room'),
    # path('room/<uuid:room_id>/', views.room_detail, name='room_detail'),

]
