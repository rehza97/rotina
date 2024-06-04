from django.urls import path
from .views import *
app_name ='doctor'
urlpatterns = [
    path('',home, name='home'),
    path('patient_list/',patient_list, name='patient_list'),
    path('search/', search, name='search'),
    path('chronic/<int:id>', chronic, name='chronic'),
]
