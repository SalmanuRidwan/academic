from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    email = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        }
    ))
    donar_name = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Full Name...'
        }
    ))
    amount = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '12,000'
        }
    ))
    description = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        }
    ))

    class Meta:
        model = Donation
        fields = ['donar_name', 'email', 'amount', 'description']
