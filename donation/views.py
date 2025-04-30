import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationForm, FundRequestForm
from .models import Donation, FundRequest
import random
from django.db.models import Count, Sum
from decimal import Decimal
from django.utils import timezone
from django.core.mail import send_mail

def home(request):
    # Get successful donations
    successful_donations = Donation.objects.filter(status='Success')

    # Total amount raised from successful donations
    total_raised = successful_donations.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')

    # Total number of donations
    donation_count = successful_donations.count()

    # Get recent donations
    recent_donations = successful_donations.order_by('-date')[:5]

    # Amount transferred: sum of all approved & active fund requests
    approved_funds = FundRequest.objects.filter(status='Approved', is_active=True)
    total_transferred = approved_funds.aggregate(total=Sum('amount_requested'))['total'] or Decimal('0.00')

    # Remaining balance = raised - transferred
    remaining_balance = total_raised - total_transferred

    context = {
        'total_raised': total_raised,
        'total_transferred': total_transferred,
        'remaining_balance': remaining_balance,
        'donation_count': donation_count,
        'recent_donations': recent_donations,
    }
    return render(request, "donation_home.html", context)

def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            payment_ref = str(random.randint(1000000000, 9999999999))

            donation = Donation.objects.create(
                donor_name=data['donor_name'],
                email=data['email'],
                amount=data['amount'],
                description=data['description'],
                payment_reference=payment_ref,
                status='Pending'
            )

            request.session['payment_ref'] = payment_ref
            return redirect('pay_with_paystack')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def pay_with_paystack(request):
    ref = request.session.get('payment_ref')
    if not ref:
        return redirect('donate')
    
    try:
        donation = Donation.objects.get(payment_reference=ref)
    except Donation.DoesNotExist:
        return redirect('donate')

    return render(request, 'confirm_payment.html', {'donation': donation})


def confirm_payment(request):
    ref = request.GET.get('reference')
    if not ref:
        return redirect('donate')

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    url = f"https://api.paystack.co/transaction/verify/{ref}"
    response = requests.get(url, headers=headers)
    result = response.json()

    if result['status'] and result['data']['status'] == 'success':
        try:
            donation = Donation.objects.get(payment_reference=ref)
            donation.status = 'Success'
            donation.save()
        except Donation.DoesNotExist:
            pass
        return render(request, 'payment_success.html', {'donation': donation})
    else:
        return render(request, 'payment_failed.html', {'ref': ref})

def transactions(request):
    donations = Donation.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'donations': donations})

#Fund Request
def request_fund(request):
    if request.method == 'POST':
        form = FundRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fund_request_success')
    else:
        form = FundRequestForm()
    return render(request, 'request_fund.html', {'form': form})

def fund_request_success(request):
    return render(request, 'fund_request_success.html')

def get_available_fund():
    total_donated = Donation.objects.filter(status='Success').aggregate(total=Sum('amount'))['total'] or 0
    total_allocated = FundRequest.objects.filter(status='Approved').aggregate(total=Sum('amount_requested'))['total'] or 0
    return total_donated - total_allocated

def fund_requests(request):
    pending = FundRequest.objects.filter(status='Pending').order_by('-date_requested')
    approved = FundRequest.objects.filter(status='Approved').order_by('-date_requested')
    deactivated = FundRequest.objects.filter(is_active=False).order_by('-date_requested')
    available_fund = get_available_fund()
    return render(request, 'fund_requests.html', {
        'pending_requests': pending,
        'approved_requests': approved,
        'deactivated_requests': deactivated,
        'available_fund': available_fund
    })

def approve_fund_request(request, pk):
    fund_request = get_object_or_404(FundRequest, pk=pk)

    if fund_request.status != 'Pending':
        return redirect('fund_requests')

    available_fund = get_available_fund()
    if available_fund >= fund_request.amount_requested:
        fund_request.status = 'Approved'
        fund_request.date_processed = timezone.now()
        fund_request.save()

        # Send approval mail to contact email
       # send_mail(
         #   subject="Your Fund Request Has Been Approved 🎉",
       #     message=f" \
        #        Hello {fund_request.organization_name},\n\n \
        #        Your fund request for ₦{fund_request.amount_requested} has been approved. \
        #        We will be reaching out shortly with next steps.\n\n \
        #        Best regards,\nDonation Team",
        #    from_email=settings.DEFAULT_FROM_EMAIL,
        #    recipient_list=[fund_request.contact_email],
       #     fail_silently=False,
       # )
      #  send_mail()

    else:
        # Redirect to insufficient funds
        return render(request, 'insufficient_funds.html', {'available_fund': available_fund})

    return redirect('fund_requests')

def deactivate_fund_request(request, pk):
    fund_request = get_object_or_404(FundRequest, pk=pk)
    fund_request.is_active = False
    fund_request.status = 'Declined'
    fund_request.save()

    # Send declination mail to contact email
    #send_mail(
     #   subject="\
     #       Your Fund Request Was Declined ❌",
     #   message=f"\
#            Hello {fund_request.organization_name},\n\n \
 #           Unfortunately, your fund request for ₦{fund_request.amount_requested} was declined. \
#            Feel free to reach out or reapply.\n\n \
 #           Best wishes,\n \
 #           Donation Team Lead \n \
 #           Ahmad Lawal.",
 #       from_email=settings.DEFAULT_FROM_EMAIL,
#        recipient_list=[fund_request.contact_email],
 #       fail_silently=False,
 #   )

    return redirect('fund_requests')

