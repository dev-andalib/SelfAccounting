from django import forms
from .models import Project, AccountType, Transaction


class CustomProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'client', 'end_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Project details...'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class CustomAccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ['name', 'type']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
        }



class CustomTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['project', 'account_type', 'debit_or_credit', 'amount', 'description']
        widgets = {
            'debit_or_credit': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Transaction details...'}),
        }
