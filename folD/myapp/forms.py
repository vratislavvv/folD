from django import forms
from .models import BankEvent

class BankEventForm(forms.ModelForm):
    class Meta:
        model = BankEvent
        fields = ['amount', 'place', 'place_type']
        widgets = {
            'place_type': forms.Select(choices=BankEvent.PLACE_TYPES),
        }
