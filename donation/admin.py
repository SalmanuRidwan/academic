from django.contrib import admin
from .models import Donation, FundRequest

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'email', 'amount', 'status', 'date', 'payment_reference')
    search_fields = ('donor_name', 'email', 'payment_reference')
    list_filter = ('status', 'date')
    ordering = ('-date',)

@admin.register(FundRequest)
class FundRequestAdmin(admin.ModelAdmin):
    list_display = (
        'organization_name', 'contact_email', 'phone_number', 
        'amount_requested', 'status', 'date_requested', 
        'date_processed', 'is_active'
    )
    search_fields = ('organization_name', 'contact_email', 'phone_number')
    list_filter = ('status', 'date_requested', 'is_active')
    ordering = ('-date_requested',)

