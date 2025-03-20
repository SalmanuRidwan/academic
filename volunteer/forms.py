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
