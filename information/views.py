from django.shortcuts import render

def home(request):
    return render(request, "information_home.html")

def twitter(request):
    return render(request, 'twitter.html')

def geolocation(request):
    return render(request, 'geolocation.html')

def user_content(request):
    return render(request, 'user_content.html')

def ai_analysis(request):
    return render(request, 'ai_analysis.html')