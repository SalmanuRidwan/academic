from django.shortcuts import render

def home(request):
    return render(request, "donation_home.html")


def payment_gateway(request):
    return render(request, 'payment_gateway.html')

def fund_tracking(request):
    return render(request, 'fund_tracking.html')

def resource_allocation(request):
    return render(request, 'resource_allocation.html')

def logistics(request):
    return render(request, 'logistics.html')