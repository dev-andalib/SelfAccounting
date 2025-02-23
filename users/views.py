from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, OTPVerificationForm, ForgetPasswordForm, SetNewPasswordForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from .models import CustomUser
import random 
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def generate_otp():
    return str(random.randint(100000, 999999))




def send_otp_email(email, otp):
    subject = "Your Signup OTP"
    message = f"Your OTP Code is: {otp}"
    from_email = "your_email@gmail.com"  # Replace with your email
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print(f"OTP sent to {email}")  # Debugging: Print to console
    except Exception as e:
        print(f"Failed to send OTP: {e}")  # Debugging: Print error to console


@login_required
def home(request, username=None):
    user = CustomUser.objects.get(username= username)
    return render(request, 'home.html', {"user":user})


def login_user(request):
    if request.user.is_authenticated:  # Keep user logged in
        return redirect(reverse('home', kwargs={'username': request.user.username}))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get authenticated user directly from the form
            login(request, user)
            return redirect(reverse('home', kwargs={'username': user.username}))  # Redirect after login

        else:
            form.add_error(None, 'Invalid login credentials')  # Show error if authentication fails

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {"form": form})

@login_required
def login_redirect_view(request):
    return redirect(reverse('home', kwargs={'username': request.user.username}))




def otpverification(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otpform = form.cleaned_data['otp']
            stored_otp = request.session.get('otp') 

            if stored_otp and otpform == stored_otp:
                del request.session['otp']  
                signup_form_data = request.session.get('signup_form_data')
                if signup_form_data:
                    signup_form = CustomUserCreationForm(signup_form_data)
                    if signup_form.is_valid():
                        signup_form.save()
                        del request.session['signup_form_data']
                        return redirect("login")
                    else:
                        form.add_error(None, 'There was an error processing your signup data.')
                else:
                    form.add_error(None, 'Signup data not found. Please try signing up again.')
            else:
                form.add_error('otp', 'Invalid OTP. Please try again.')
    else:
        form = OTPVerificationForm()
    return render(request, "verifyOTP.html", {'form': form})





def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            otp = generate_otp()
            email = form.cleaned_data['email']
            send_otp_email(email, otp)
            request.session['otp'] = otp
            request.session['signup_form_data'] = request.POST
            return redirect("otpverification")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})






def forgetPassword(request):
    if request.method == "POST":
        if 'email' in request.POST:
            form = ForgetPasswordForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                otp = generate_otp()
                send_otp_email(email, otp)
                request.session['forgot_email'] = email
                request.session['otp'] = otp
                request.session.set_expiry(7 * 60)  # Set expiry time to 7 minutes
                return redirect("forgetPassword")
            messages.error(request, "Invalid email address. Please try again.")
        
        elif 'otp' in request.POST and 'forgot_email' in request.session:
            form = OTPVerificationForm(request.POST)
            if form.is_valid():
                otpform = form.cleaned_data['otp']
                stored_otp = request.session.get('otp')

                if stored_otp and otpform == stored_otp:
                    del request.session['otp']
                    request.session['otp_verified'] = True
                    request.session.set_expiry(7 * 60)  # Reset expiry for next step
                    return redirect("forgetPassword")
                messages.error(request, "Invalid OTP. Please try again.")
            messages.error(request, "Invalid OTP format. Please try again.")
        
        elif 'new_password' in request.POST and 'otp_verified' in request.session:
            form = SetNewPasswordForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password']
                email = request.session.get('forgot_email')
                try:
                    user = CustomUser.objects.get(email=email)
                    user.set_password(new_password)
                    user.save()
                    request.session.flush()  # Clear session completely after reset
                    messages.success(request, "Your password has been reset successfully. Please log in.")
                    return redirect("login")
                except CustomUser.DoesNotExist:
                    messages.error(request, "User not found. Please try again.")
            messages.error(request, "Invalid password. Please try again.")

    if 'forgot_email' not in request.session:
        form = ForgetPasswordForm()
    elif 'otp_verified' not in request.session:
        form = OTPVerificationForm()
    else:
        form = SetNewPasswordForm()

    return render(request, "forgetPassword.html", {"form": form})




def logout_view(request):
    logout(request)
    return redirect('login') 