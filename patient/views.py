from django.contrib.auth.decorators import login_required
from accounts.form import *
from accounts.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='login')
def home(request):
    context = {}
    try:
        # Get the latest appointment for the logged-in user
        appointment = Appointment.objects.filter(patient=request.user , validate = True).last()
        if appointment:
            context['appointment'] = appointment
        else:
            context['err'] = "You don't have any appointment yet, you can create one from make appointment or contact us to reserve one for you. \n in case you already reserve one please wait till your appointment get accepted"
    except ObjectDoesNotExist:
        context['err'] = "An error occurred while retrieving your appointments."

    return render(request, 'patient/index.html', context)


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