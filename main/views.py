from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

import json

from .models import CustomUser, WishGame
from .forms import CustomUserCreationForm, CustomUserForm

def dashboard(request):
    return render(request, 'main/dashboard.html')

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user,
    }
    return render(request, 'main/profile.html', context)

@login_required
def edit_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user,
        'user_form': CustomUserForm,
    }
    if request.method == 'GET':
        return render(request, 'main/edit_profile.html', context)
    elif request.method == 'POST':
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html',
            {"form": CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))

@login_required        
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
    
@login_required
def addToList(request):
    if request.method =='POST':
        data = json.loads(request.body)
        WishGame.objects.create(
            wisher = request.user,
            api_id = data.get('game')
        )
        return render(request, 'main/dashboard.html')
    
@login_required
def removeGame(request):
    data = json.loads(request.body)
    api_id = data.get('game')
    WishGame.objects.get(api_id=api_id).delete()
    return render(request, 'main/dashboard.html')
    
@login_required
def getWishedId(request):
    id_objects = WishGame.objects.all()
    ids = []
    for id_object in id_objects:
        ids.append(id_object.api_id)
    data = {
        'api_id': ids
    }
    return JsonResponse(data)