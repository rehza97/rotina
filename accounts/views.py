from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .form import AccountUpdateForm, CustomUserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# @login_required(login_url='login')


def creation_page(request):
    if request.user.is_authenticated:
        if request.user.is_patient:
            return redirect('patient:home')
        elif request.user.is_secretary:
            return redirect('secretary:home')
        elif request.user.is_doctor:
            return redirect('doctor:home')
        else:
            return redirect('admn:home')
    creation = CustomUserCreationForm()
    context = {
        'creation': creation
    }
    return render(request, 'accounts/login.html', context)


def create_account(request):
    if request.user.is_authenticated:
            return redirect('patient:profile_creation')
    if request.method == 'POST':
        creation = CustomUserCreationForm(request.POST)
        if creation.is_valid():
            user = creation.save(commit=False)
            user.is_patient = True  
            user.email = user.username
            user.save()
            return redirect('log_reg_page') 
        else:
            context = {
                'creation': creation
            }
            return render(request, 'accounts/login.html', context)
    else:
        creation = CustomUserCreationForm()
        context = {
            'creation': creation
        }
        return render(request, 'accounts/login.html', context)

def login_url(request):
    if request.user.is_authenticated:
        if request.user.is_patient:
            return redirect('patient:home')
        elif request.user.is_secretary:
            return redirect('secretary:home')
        elif request.user.is_doctor:
            return redirect('secretary:home')
        else:
            return redirect('secretary:home')
        
    creation = CustomUserCreationForm()
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('patient:profile_creation')
        else:

            context = {
                'error': 'Invalid email or password',
                'creation': creation
                }
            return render(request, 'accounts/login.html',context)
    else:
        return render(request, 'accounts/login.html')
    
def logout_user(resquet):
    logout(resquet)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    return render(request , 'accounts/my_profile.html')

@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
            form.profile = True
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')  # Assuming you have a profile view
    else:
        form = AccountUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'patient/profile_creation.html', context)


def user_profile(request,pk):
    persone = get_object_or_404(Account, id=pk)
    
    context= {
        'persone': persone
    }
    
    return render(request,'accounts/user_profile.html',context)