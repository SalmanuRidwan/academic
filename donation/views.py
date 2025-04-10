from django.shortcuts import render, redirect
from .forms import DonationForm

def home(request):
    return render(request, "donation_home.html")


def payment_gateway(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Try to get or create a user
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': email}
            )

            # If user exists but no Volunteer record, create one
            if not hasattr(user, 'volunteer'):
                volunteer = form.save(commit=False)
                volunteer.user = user
                volunteer.save()
                # # Optional: add a message or redirect
                return redirect('volunteer_thank_you')

            form.add_error(None, 'A volunteer profile already exists for this user.')

    else:
        form = DonationForm()
    return render(request, 'payment_gateway.html', {"form": form})

def fund_tracking(request):
    return render(request, 'fund_tracking.html')

def resource_allocation(request):
    return render(request, 'resource_allocation.html')

def logistics(request):
    return render(request, 'logistics.html')