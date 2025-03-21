from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='volunteer_home'),
    path('register-volunteer/', views.register_volunteer, name='register_volunteer'),
    path('skill-match/', views.skill_matching, name="skill_match"),
    path('chat-room/', views.chat_room, name="chat_room"),
    path('task-management/', views.task_management, name="task_management"),
]
