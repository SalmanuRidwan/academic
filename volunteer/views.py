from django.shortcuts import render

def home(request):
    return render(request, "volunteer_home.html")

def register_volunteer(request):
    return render(request, 'register_volunteer.html')

def skill_matching(request):
    return render(request, "skill_matching.html")

def chat_room(request):
    return render(request, "chat_room.html")

def task_management(request):
    return render(request, 'task_management.html')