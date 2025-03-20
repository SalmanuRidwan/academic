from django import forms
from .models import Report, Media

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'tags', 'location']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['file']
