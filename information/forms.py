from django import forms
from .models import Report, Tag

class ReportForm(forms.ModelForm):
    title = forms.CharField(
        max_length=154,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title...'
        })
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description...',
            'rows': 4
        })
    )

    location = forms.CharField(
        max_length=154,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Location...'
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Report
        fields = ['title', 'description', 'location', 'tags']
