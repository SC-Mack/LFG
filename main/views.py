from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import CustomUserCreationForm

def dashboard(request):
    return render(request, 'main/dashboard.html')

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'main/profile.html', {'user': user})

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        
def password_switch(request):
    if request.method == "GET":
        return render(
            request, "registration/password-switch.html",
            {"form": PasswordChangeForm}
        )
    elif request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))