from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, OTPVerificationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate
import random, smtplib
from django.core.mail import send_mail
from django.contrib import messages






def generate_otp():
    return str(random.randint(100000, 999999))



from django.core.mail import send_mail

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



def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            

            if authenticate(username = username, password = password) != None:
                return redirect(home) 
            
            else:
                form.add_error(None, 'Invalid login credentials')
                
        else:
            form.add_error(None, 'Please correct the errors below')        
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})



def otpverification(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otpform = form.cleaned_data['otp']
            stored_otp = request.session.get('otp')  # Retrieve OTP from session

            if stored_otp and otpform == stored_otp:  # Compare OTPs
                # OTP is valid
                del request.session['otp']  # Clear OTP from session

                # Retrieve the signup form data from the session
                signup_form_data = request.session.get('signup_form_data')
                if signup_form_data:
                    # Create a form instance with the retrieved data
                    signup_form = CustomUserCreationForm(signup_form_data)
                    if signup_form.is_valid():
                        # Save the user to the database
                        user = signup_form.save()
                        # Optionally, you can log the user in here if needed
                        # from django.contrib.auth import login
                        # login(request, user)

                        # Clear the signup form data from the session
                        del request.session['signup_form_data']

                        # Redirect to login page after successful verification
                        return redirect("login")
                    else:
                        # Handle the case where the form is not valid
                        form.add_error(None, 'There was an error processing your signup data.')
                else:
                    # Handle the case where the signup form data is not found in the session
                    form.add_error(None, 'Signup data not found. Please try signing up again.')
            else:
                # OTP is invalid
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

            # Store OTP and form data in session for verification
            request.session['otp'] = otp
            request.session['signup_form_data'] = request.POST

            # Redirect to OTP verification page
            return redirect("otpverification")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})




def forgetPassword(request):
    return render(request, )