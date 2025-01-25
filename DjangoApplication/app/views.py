from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import re


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "app/login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password validation rules
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long")
        elif not re.search(r"[A-Za-z]", password):  # Check for alphabet
            messages.error(request, "Password must contain at least one alphabet")
        elif not re.search(r"[0-9]", password):  # Check for digit
            messages.error(request, "Password must contain at least one digit")
        elif not re.search(r"[@$!%*?&]", password):  # Check for special character
            messages.error(request, "Password must contain at least one special character")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Your account has been successfully activated!")
            return redirect("login")

    return render(request, "app/signup.html")


def forgot_password_view(request):
    return render(request, "app/forgot_password.html")


@login_required
def change_password_view(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        if request.user.check_password(old_password):
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, "Password changed successfully")
                return redirect("login")
            else:
                messages.error(request, "New passwords do not match")
        else:
            messages.error(request, "Old password is incorrect")
    return render(request, "app/change_password.html")


@login_required
def dashboard_view(request):
    return render(request, "app/dashboard.html", {"username": request.user.username})


@login_required
def profile_view(request):
    return render(request, "app/profile.html", {"user": request.user})


def logout_view(request):
    logout(request)
    return redirect("login")
