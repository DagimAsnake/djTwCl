from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm, ChangePasswordForm, CustomRegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
         registerForm = CustomRegisterForm(request.POST)
         if registerForm.is_valid():
            registerForm.save()
            messages.success(request, ('New User Account Created, Login To Get Started'))
            return redirect('/account/register')
    else:
        registerForm = CustomRegisterForm()
    return render(request, "register.html", {'registerForm': registerForm })


def editUser(request, userId):
    if request.method == 'POST':
        if 'password' in request.POST:
            password_form = ChangePasswordForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
        else:
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        password_form = ChangePasswordForm(user=request.user)
    return render(request, 'edit.html', {'form': form, 'password_form': password_form})
