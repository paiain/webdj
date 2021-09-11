
from django.urls import path
from app.views import  doctor, index, patient


urlpatterns = [
    path('', index,  name='index'),
    path('patient/', patient,  name='patinent'),
    path('doctor', doctor,  name='doctor')
]
