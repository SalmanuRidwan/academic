from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="information_home"),
    path('submit-report/', views.submit_report, name='submit_report'),
    path('report-success/', views.report_success, name='report_success'),
    path('reports/', views.reports, name='reports_list'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
]
