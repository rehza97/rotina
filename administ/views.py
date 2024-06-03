from accounts.models import *
from .forms import *
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def home(request):
    return render(request ,'administrateur/index.html')

def create_doctor(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True  
            user.email = user.username
            user.profile = True
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = RegistrationForm()
    return render(request, 'administrateur/profile_creation_doc.html', {'form': form})

def list_doctor(request):
    docs = Account.objects.filter(is_doctor=True)
    context = {
        'docs' : docs
    }
    return render(request , 'administrateur/docs.html',context)


def create_sect(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_secretary = True  
            user.email = user.username
            user.profile = True
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = RegistrationForm()
    return render(request, 'administrateur/profile_creation_sect.html', {'form': form})

def list_sect(request):
    sects = Account.objects.filter(is_secretary=True)
    context = {
        'sects' : sects
    }
    return render(request , 'administrateur/sects.html',context)


def create_patient(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True  
            user.email = user.username
            user.profile = True
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = RegistrationForm()
    return render(request, 'administrateur/profile_creation.html', {'form': form})

def patient_list(request):
    patients = Account.objects.filter(is_patient=True)
    context = {
        'patients' : patients
    }
    return render(request , 'administrateur/patients.html',context)



