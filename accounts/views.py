from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

from .forms import RegisterForm, ProfileUpdateForm
from .models import LoginOTP


# =========================
# OTP FUNCTIONS
# =========================

def send_login_otp(user):
    otp = str(random.randint(100000, 999999))

    
    LoginOTP.objects.create(
        user=user,
        otp_code=otp
    )

   
    print("\n================ OTP LOGIN =================")
    print("User:", user.username)
    print("OTP :", otp)
    print("===========================================\n")

 
    send_mail(
        subject="Your Login Verification Code",
        message=f"Your OTP is: {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email] if user.email else [],
        fail_silently=True,  
    )


# =========================
# LOGIN + OTP
# =========================

@ratelimit(key='ip', rate='5/m', block=False)
def login_with_otp(request):

    if getattr(request, "limited", False):
        return render(request, "403.html", status=403)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            send_login_otp(user)
            return redirect("verify_otp")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


@login_required
def verify_otp(request):
    if request.method == "POST":
        otp_input = request.POST.get("otp")

        otp_record = LoginOTP.objects.filter(
            user=request.user,
            otp_code=otp_input,
            is_verified=False
        ).first()

        if otp_record:
            otp_record.is_verified = True
            otp_record.save()
            messages.success(request, "Login verified successfully!")
            return redirect("home")
        else:
            messages.error(request, "Invalid or expired OTP")

    return render(request, "accounts/verify_otp.html")


# =========================
# REGISTER / LOGOUT
# =========================

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


# =========================
# PROFILE & PASSWORD
# =========================

@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("edit_profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "accounts/edit_profile.html", {"form": form})


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect("change_password")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "accounts/change_password.html", {"form": form})


# =========================
# SECURE API (EXTRA)
# =========================

@csrf_exempt
@login_required
def secure_booking_api(request):
    if request.method == "GET":
        return JsonResponse({"message": "Secure booking API works!"})

    return JsonResponse({"error": "Invalid request"}, status=400)
