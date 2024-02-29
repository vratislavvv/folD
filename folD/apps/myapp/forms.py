from django import forms
from .models import BankEvent, Income, Saving, Investment, Subscribtion

class BankEventForm(forms.ModelForm):
    class Meta:
        model = BankEvent
        fields = ['bankevent_amount', 'bankevent_place', 'bankevent_place_type']
        widgets = {
            'place_type': forms.Select(attrs={'class': 'EXP_input'}),
        }

    def __init__(self, *args, **kwargs):
        super(BankEventForm, self).__init__(*args, **kwargs)
        self.fields['place_type'].choices = [('', 'Select Place Type')] + list(BankEvent.PLACE_TYPES)

class SubscribtionForm(forms.ModelForm):
    class Meta:
        model = Subscribtion
        field = ['subscribtion_amount', 'subscribtion_place', 'subscribtion_place_type']
        widgets= {
            'subscribtion_amount': forms.NumberInput(attrs={'class': 'x', 'placeholder': 'Amount'}),
        }

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_amount', 'income_place', 'income_wageday']
        widgets = {
            'income_amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
            'income_place': forms.TextInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Place'}),
            'income_wageday': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Wage day'}),
        }

class AddSavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ['saving_amount']
        widgets = {
            'saving_amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
        }

class AddInvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['investment_amount']
        widgets = {
            'investment_amount': forms.NumberInput(attrs={'class': 'INC_incform_input', 'placeholder': 'Amount'}),
        }

