from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm



class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username', 'password1', 'password2', 'email', 'birthday', 'phone', 
            'street', 'commun', 'wilaya', 'postal_code', 'gender', 'num_chifa', 
            'blood_type','first_name','last_name','specialty'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'commun': forms.TextInput(attrs={'class': 'form-control'}),
            'wilaya': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'num_chifa': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
        }
        
        


class UserProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Account
        fields = [
            'username', 'email', 'birthday', 'phone', 
            'street', 'commun', 'wilaya', 'postal_code', 
            'gender', 'num_chifa', 'blood_type', 'specialty',
            'password', 'password_confirm', 'first_name', 'last_name'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'commun': forms.TextInput(attrs={'class': 'form-control'}),
            'wilaya': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'num_chifa': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
