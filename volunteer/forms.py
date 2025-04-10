from django import forms
from .models import Volunteer

class VolunteerSignupForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['bio', 'skills', 'availability', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skills'].widget.attrs.update({'placeholder': 'e.g., First Aid, Cooking'})
        self.fields['availability'].widget.attrs.update({'placeholder': 'e.g., Weekends, Evenings'})
        self.fields['location'].widget.attrs.update({'placeholder': 'City or Region'})

class VolunteerRegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email...'
        }
    ))
    username = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username...'
        }
    ))
    location = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Location...'
        }
    ))
    availability = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'work-days, weekend...'
        }
    ))
    skills = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Skills...'
        }
    ))
    bio = forms.CharField(max_length=154, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Bio...'
        }
    ))

    class Meta:
        model = Volunteer
        fields = ['username', 'email', 'bio', 'skills', 'location', 'availability', 'is_available']
