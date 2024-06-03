from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')

class AccountUpdateForm(UserChangeForm):
    class Meta:
        model = Account
        fields = [
            'username', 'email', 'first_name', 'last_name', 'birthday', 'phone', 'street', 
            'commun', 'wilaya', 'postal_code',  
            'gender', 'num_chifa', 'blood_type', 
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'note', 'date']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

        
class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'note', 'date','validate']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

