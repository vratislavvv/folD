from django import forms
from .models import BankEvent, Income, Saving, Investment

class BankEventForm(forms.ModelForm):
    class Meta:
        model = BankEvent
        fields = ['amount', 'place', 'place_type']
        widgets = {
            'place_type': forms.Select(attrs={'class': 'EXP_input'}),
        }

    def __init__(self, *args, **kwargs):
        super(BankEventForm, self).__init__(*args, **kwargs)
        self.fields['place_type'].choices = [('', 'Select Place Type')] + list(BankEvent.PLACE_TYPES)

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount1', 'place1', 'wageday']
        widgets = {
            'amount1': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place1': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'wageday': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Wage day'}),
        }

class AddSavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ['amount2', 'place2']
        widgets = {
            'amount2': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place2': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
        }

class AddInvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['amount3', 'place3', 'interest']
        widgets = {
            'amount3': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place3': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'interest': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Interest'}),
        }

