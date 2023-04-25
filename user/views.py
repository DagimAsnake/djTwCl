from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages

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
    