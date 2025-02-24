from django.urls import path
from .views import login_user, signup, home, otpverification, login_redirect_view, forgetPassword, logout_view, editAcc

urlpatterns = [
    path('', login_user, name='login_user'),
    path("signup/", signup, name="signup"),
    path("home/<str:username>/", home, name = "home"),
    path("otp/", otpverification, name = 'otpverification'),
    path("forget_password/", forgetPassword, name="forgetPassword"),
    path('auth/logout/', logout_view, name='logout_view'),
    path('redirect-after-login/', login_redirect_view, name='login_redirect'),
    path('editAcc/', editAcc, name = 'editAcc')
]