from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='donation_home'),
    path('payment-gateway/', views.payment_gateway, name="payment_gateway"),
    path('resource-allocation/', views.resource_allocation, name='resource_allocation'),
    path('logistics/', views.logistics, name='logistics'),
    path('fund-tracking/', views.fund_tracking, name='fund_tracking')
]

