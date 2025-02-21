from django.urls import path
from .views import login, signup, home, otpverification, forgetPassword

urlpatterns = [
    path('', login, name='login'),
    path("signup/", signup, name="signup"),
    path("home/<str:username>/", home, name = "home"),
    path("otp/", otpverification, name = 'otpverification'),
    path("forget_password/", forgetPassword, name="forgetPassword"),
    
]