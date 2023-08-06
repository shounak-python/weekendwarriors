from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def homepage(request):
    return render(request, "home/homepage.html")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        email = form["email"]
        if form.is_valid():
            if not User.objects.filter(email=email):
                user = form.save()

                # logs in user
                login(request, user)

                messages.success(request, "Success: Registration successful.")
                return redirect("home:login")
        messages.error(request, "Error: Unsuccessful registration.")
    form = NewUserForm()
    ctx = {"register_form": form}
    return render(request, "registration/register.html", ctx)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Success: Logged in as {username}")
                return redirect("home:homepage")
            else:
                messages.error(request, "Error: Invalid username or/and password")
        else:
            messages.error(request, "Error: Invalid username or/and password")
    form = AuthenticationForm()
    ctx = {"form": form}
    return render(request, "registration/login.html", ctx)


def logout_request(request):
    logout(request)
    messages.success(request, "Success: Logged out successfully")
    return redirect("home:homepage")