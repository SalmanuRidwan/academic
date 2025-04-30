from django import forms
from .models import Donation, FundRequest


class DonationForm(forms.ModelForm):
    email = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email'}
    ))
    donor_name = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Full Name...'}
    ))
    amount = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '12,000'}
    ))
    description = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Description'}
    ))

    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'amount', 'description']


class FundRequestForm(forms.ModelForm):
    organization_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Organization Name'
        })
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contact Email'
        })
    )
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        })
    )
    amount_requested = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount Requested'
        })
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Purpose of the funding...',
            'rows': 4
        })
    )

    class Meta:
        model = FundRequest
        fields = ['organization_name', 'contact_email', 'phone_number', 'amount_requested', 'description']
