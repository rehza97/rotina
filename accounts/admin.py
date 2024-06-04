from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Secretary)
admin.site.register(Doctor)
admin.site.register(Chronic)
admin.site.register(Paymenets)
admin.site.register(MedAnalyses)
admin.site.register(MedicalCert)
admin.site.register(Meddication)
admin.site.register(MedFam)
admin.site.register(Prescription)