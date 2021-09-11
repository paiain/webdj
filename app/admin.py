
from django.contrib import admin
from app.models import Doctor, Hospital, Patient


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'skill']


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name', 'age', 'sex']
