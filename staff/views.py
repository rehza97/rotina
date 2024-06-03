from accounts.models import *
from accounts.form import *
from .forms import *
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff(user):
    return  user.is_secretary

# def is_doctor(user):
#     return user.is_doctor 

# def is_patient(user):
#     return  user.is_patient


@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def home(request):
    return render(request,'staff/index.html')

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def create_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True  
            user.email = user.username
            user.profile = True
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = PatientRegistrationForm()
    return render(request, 'staff/profile_creation.html', {'form': form})

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def patient_list(request):
    patients = Account.objects.filter(is_patient=True)
    context = {
        'patients' : patients
    }
    return render(request , 'staff/patients.html',context)

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def update_patient(request,id):
    user = Account.objects.get(id=id)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            
            
            password = form.cleaned_data.get('password')
            if not password == None:
                if password:
                    user.set_password(password)

            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')  # Redirect to the profile page or another page
    else:
        form = UserProfileUpdateForm(instance=user)
    return render(request, 'staff/profile_update.html', {'form': form})

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def delete_patient(request, id):
    patient = get_object_or_404(Account, id=id, is_patient=True)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient account deleted successfully.')
        return redirect('secretary:patient_list')  

    context = {
        'patient': patient
    }
    return render(request, 'staff/delete_patient.html', context)


@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def archive_patient(request,id):
    pass


@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def create_appointment(request):
    accounts = Account.objects.filter(is_patient=True)

    if request.method == 'POST':
        patient = request.POST.get('patient')
        print(patient)
        patient = Account.objects.get(username=patient)
        print(patient)
        date = request.POST.get('date')
        note = request.POST.get('note')
        accepte = request.POST.get('accepte')
        appointment = Appointment.objects.create(
            patient = patient,
            note = note,
            date = date,
            validate = True
        )
        messages.success(request, 'Appointment created successfully.')
        return redirect('secretary:home')  
    else:
        form = AppointmentForm()
    context =  {
        'form': form,
        'accounts': accounts,
        }
    return render(request, 'staff/add-appointmenets.html', context)


@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def appointment_list(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment' : appointment
    }
    return render(request , 'staff/appointments.html', context)

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def update_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    
    if request.method == 'POST':
        form = UpdateAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('your_redirect_url')  # Replace with your redirect URL
    else:
        form = UpdateAppointmentForm(instance=appointment)
    
    context = {
        'form': form,
        'appointment': appointment,
    }
    return render(request, 'staff/update_appointments.html', context)

@login_required(login_url='login') 
@user_passes_test(is_staff,login_url='home')
def delete_appointment(request,id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('secretary:appointment_list')

def archive_appointment(request,id):
    pass

def create_payement(request):
    pass

def payement_list(request):
    pass

def update_payement(request,id):
    pass

def delete_payement(request,id):
    pass

def archive_payement(request,id):
    pass


