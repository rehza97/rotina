from django.urls import path
from .views import *
app_name = 'admn'
urlpatterns = [
    path('home/',home,name='home'),
    path('create_doctor/',create_doctor,name='create_doctor'),
    path('list_doctor/',list_doctor,name='list_doctor'),
    path('create_sect/',create_sect,name='create_sect'),
    path('list_sect/',list_sect,name='list_sect'),
    path('create_patient/',create_patient,name='create_patient'),
    path('patient_list/',patient_list,name='patient_list'),
]
