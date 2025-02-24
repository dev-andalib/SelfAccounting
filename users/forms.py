from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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




class ForgetPasswordForm(forms.Form):
    email = forms.EmailField (
        label="Enter the email associated with your account",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}))
    




class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter new password"}),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter new password"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data




class EditAccountForm(UserChangeForm):
    # Define fields to be editable
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ChoiceField(choices=[('accountant', 'Accountant')])  # Add more roles if needed

    # Don't include the email field for editing
    email = forms.EmailField(required=False, widget=forms.HiddenInput(), disabled=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'role']  # Only include fields you want to edit

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
