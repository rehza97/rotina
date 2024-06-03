from django.urls import path
from .views import *

app_name = 'patient'

urlpatterns = [
    path('', home, name='home'),
    path('profile-creation', make_profile, name='profile_creation'),
    path('create_appointment', create_appointment, name='create_appointment'),
]