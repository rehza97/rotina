from django.urls import path
from .views import *
app_name = 'secretary'
urlpatterns = [
    path('',home,name="home"),
    
    # patient
    path('create_patient/',create_patient,name="create_patient"),
    path('patient_list/',patient_list,name="patient_list"),
    path('update_patient/<int:id>',update_patient,name="update_patient"),
    path('delete_patient/<int:id>',delete_patient,name="delete_patient"),
    path('archive_patient/<int:id>',archive_patient,name="archive_patient"),
    # appointment
    path('create_appointment/',create_appointment,name="create_appointment"),
    path('appointment_list/',appointment_list,name="appointment_list"),
    path('update_appointment/<int:id>',update_appointment,name="update_appointment"),
    path('delete_appointment/<int:id>',delete_appointment,name="delete_appointment"),
    path('archive_appointment/<int:id>',archive_appointment,name="archive_appointment"),
    # payement
    
    path('create_payement/',create_payement,name="create_payement"),
    path('payement_list/',payement_list,name="payement_list"),
    path('update_payement/',update_payement,name="update_payement"),
    path('update_payement/',update_payement,name="update_payement"),
    path('update_payement/',update_payement,name="update_payement"),
    # path('make_appointmenets/',make_appointmenets,name="make_appointmenets"),
    # path('make_payement/',make_payement,name="make_payement"),
]
