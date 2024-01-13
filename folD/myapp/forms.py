from django import forms
from .models import BankEvent, Income, Savings, Investments

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
        fields = ['amount', 'place', 'wageday']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'wageday': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Wage day'}),
        }

class AddSavingForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['amount', 'place']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
        }

class AddInvestmentForm(forms.ModelForm):
    class Meta:
        model = Investments
        fields = ['amount', 'place', 'interest']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'place': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'interest': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Interest'}),
        }

