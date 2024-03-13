from django import forms
from .models import BankEvent, Income, Saving, Investment, Subscribtion
from .models_data import PLACE_TYPES

class BankEventForm(forms.ModelForm):
    class Meta:
        model = BankEvent
        fields = ['amount', 'place', 'place_type']
        widgets = {
            'place_type': forms.Select(attrs={'class': 'EXP_input'}),
        }

    def __init__(self, *args, **kwargs):
        super(BankEventForm, self).__init__(*args, **kwargs)
        self.fields['place_type'].choices = [('', 'Select Place Type')] + list(PLACE_TYPES)

class SubscribtionForm(forms.ModelForm):
    class Meta:
        model = Subscribtion
        fields = ['amount', 'place', 'place_type', 'repetition']
        widgets= {
            'amount': forms.NumberInput(attrs={'class': 'x', 'placeholder': 'Amount'}),
        }

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'place', 'wageday']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'wageday': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Wage day'}),
        }

class AddSavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
        }

class AddInvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['key']
        widgets = {
            'key': forms.TextInput(attrs={'class': 'trading212_input', 'placeholder': 'Key'}),
        }
