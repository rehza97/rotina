from django.shortcuts import render
from accounts.models import *
from django.db.models import Q
from django_filters.views import FilterView
from django.views.generic import ListView
from .filters import *
# Create your views here.
def home(request):
    return render(request , 'doctor/index.html')


def patient_list(request):
    patients = Account.objects.filter(is_patient=True)
    context = {
        'patients' : patients
    }

    return render(request , 'doctor/patients.html',context)


def search(request):
    # Retrieve all patients
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        # Filter patients based on the provided username
        patients = Account.objects.filter(is_patient=True, username=username).first()
    else:
        patients = f'sorry the patient u r looking for doesn\'t in database '
    # Apply additional filtering based on GET parameters
    # myfilter = PatientFilter(request.GET, queryset=patients)
    # patients = myfilter.qs
    # print(patients)
    context = {
        # 'myfilter': myfilter,
        'patients': patients,
    }
    return render(request, 'doctor/search.html', context)

# def search_accounts(request):
#     email = request.POST.get('search')
#     if request.POST == 'POST':
        
#     context = {
     
#     }
#     return render(request, 'search_results.html', context)