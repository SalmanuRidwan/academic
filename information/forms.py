from django import forms
from .models import Report, Media

class ReportForm(forms.ModelForm):
    title = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title...'
        }
    ))
    description = forms.CharField(max_length=154, required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Description...'
        }
    ))
    location = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Location...'
        }
    ))
    class Meta:
        model = Report
        fields = ['title', 'description', 'location']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['file']
