from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='donation_home'),
    path('donate/', views.donate, name="donate"),
    path('confirm-payment/', views.confirm_payment, name="confirm_payment"),
    path('payment/', views.pay_with_paystack, name='pay_with_paystack'),
    path('transactions/', views.transactions, name='transactions'),
     
    # Fund Request
    path('request-fund/', views.request_fund, name='request_fund'),
    path('request-fund/success/', views.fund_request_success, name='fund_request_success'),
    path('fund-requests/', views.fund_requests, name='fund_requests'),
    path('approve-request/<int:pk>/', views.approve_fund_request, name='approve_fund_request'),
    path('deactivate-request/<int:pk>/', views.deactivate_fund_request, name='deactivate_fund_request'),
]
