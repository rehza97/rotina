from django.shortcuts import render
from accounts.models import *
from django.db.models import Q
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
    myfilter = Account.objects.filter(is_patient=True)
    patients = None
    full_name = ''
    if request.method == 'POST':
        full_name = request.POST.get('full_name')     
        print('________________________________')
        print(full_name)
        names = full_name.split(' ')
        if len(names) == 2:
            print(names)
            first_name = names[1]
            last_name = names[0]
            # Filter patients based on the provided full name
            patients = Account.objects.filter(is_patient=True, first_name__icontains=first_name, last_name__icontains=last_name).first()
            print(patients)
        else:
            patients = f'Sorry, the patient you are looking for is not in the database.'

    context = {
        'myfilter': myfilter,
        'patients': patients,
    }
    return render(request, 'doctor/search.html', context)

def consiltation(request):
    pass

def chronic(request,id):
    patients = Account.objects.get(id=id)
    patient = Patient.objects.get(user = patients)
    if request.method == 'POST':
        ch = request.POST.get('chronic')
        chronic = Chronic.objects.create(name = ch)
        patient.chronic = chronic
        patient.save()
        context = {'patients': patients,'patient': patient,}
        return render(request, 'doctor/search.html', context)
    context = {'patients': patients,'patient': patient,}
    return render(request, 'doctor/search.html',context)
    

def analyses(request,id):
    patients = Account.objects.get(id=id)
    
    if request.method == 'POST':
        analise = request.POST.get('analise')
        date = request.POST.get('date')
        analyses = MedAnalyses.objects.create(
            patient = patients,
            meds = analise,
            date = date
        )
        
        return render(request, 'doctor/search.html', context)
    context = {'patients': patients,'analyses': analyses,}
    return render(request, 'doctor/search.html',context)
    
     

    
def medicaments(request):
    pass

def certaficat(request):
    pass



