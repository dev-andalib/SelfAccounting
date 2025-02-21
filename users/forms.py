from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser





class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ChoiceField(choices=[('accountant', 'Accountant')])
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']

    def clean_email(self):
        """Ensure email is unique and meets custom validation criteria."""
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'accountant'  
        if commit:
            user.save()
        return user
    



class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        max_length=6, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OTP'})
    )

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        if not otp.isdigit() or len(otp) != 6:
            raise forms.ValidationError("Invalid OTP. Please enter a 6-digit number.")
        return otp
