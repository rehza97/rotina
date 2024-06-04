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
        fields = ['patient', 'note', 'date', 'time', 'validate', 'paied']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

        
class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'note', 'date', 'time', 'validate', 'paied']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
