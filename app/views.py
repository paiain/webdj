from django.shortcuts import render
from app.models import Hospital, Patient, Doctor

# Create your views here.


contex1 = {}
hospital = Hospital.objects.all()
contex1['hospitals'] = hospital

contex2 = {}
patient = Patient.objects.all()
contex2['patients'] = patient

contex3 = {}
doctor = Doctor.objects.all()
contex3['doctors'] = doctor


def patient(request):
    return render(request, 'patient.html', contex2)


def doctor(request):
    return render(request, 'doctor.html', contex3)


def index(request):
    return render(request, 'index.html', contex1)
