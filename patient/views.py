from django.contrib.auth.decorators import login_required
from accounts.form import *
from accounts.models import *
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request,'patient/index.html')

def make_profile(request):
    if  request.user.profile:
        pass
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
            form.profile = True
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')  
    else:
        form = AccountUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'patient/profile_creation.html', context)


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user  # Set the patient as the logged-in user
            appointment.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('patient:home')  # Redirect to a list of appointments or another page
    else:
        form = AppointmentForm()
    return render(request, 'patient/create_appointment.html', {'form': form})