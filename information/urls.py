from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='information_home'),
    path('twitter/', views.twitter, name='twitter'),
    path('geolocation/', views.geolocation, name='geolocation'),
    path('user-content/', views.user_content, name='user_content'),
    path('ai-analysis/', views.ai_analysis, name='ai_analysis'),
]
