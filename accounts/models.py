from django.contrib.auth.models import AbstractUser
from django.db import models

SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

BLOOD_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Account(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    commun = models.CharField(max_length=100, blank=True, null=True)
    wilaya = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=SEX_CHOICES, blank=True, null=True)
    num_chifa = models.CharField(max_length=150, unique=True, blank=True, null=True)
    blood_type = models.CharField(max_length=100, choices=BLOOD_CHOICES, blank=True, null=True)
    profile = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False, blank=True, null=True)
    is_doctor = models.BooleanField(default=False, blank=True, null=True)
    is_secretary = models.BooleanField(default=False, blank=True, null=True)
    specialty = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email

class Patient(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='patient_profile')
    chronic = models.ForeignKey('Chronic', on_delete=models.CASCADE)
    # Add additional fields specific to patients

class Secretary(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='secretary_profile')
    # Add additional fields specific to secretaries

class Doctor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='doctor_profile')
    # Add additional fields specific to doctors

class Chronic(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    validate = models.BooleanField(default=False, blank=True, null=True)
    paied = models.ForeignKey('Paymenets' , on_delete=models.CASCADE,blank=True, null=True)



class Paymenets(models.Model):
    price = models.CharField(max_length=20)

    

class MedicalCert(models.Model):
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField()
    date = models.DateField()

class MedAnalyses(models.Model):
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    meds = models.TextField()
    date = models.DateField()

class Prescription(models.Model):
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    meds = models.ForeignKey('Meddication', on_delete=models.CASCADE, related_name='prescriptions')
    date = models.DateField()
    med = models.ManyToManyField('Meddication', related_name='prescribed_medications')

class MedFam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class Meddication(models.Model):
    family = models.ForeignKey(MedFam, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
