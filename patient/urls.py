from django.urls import path
from patient.views import *

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('<int:id>/details/', patient_details, name="patient_details"),
    path('<int:id>/edit/', patient_edit, name="patient_edit"),
    path('add/', patient_add, name="patient_add"),
    path('<int:id>/delete/', patient_delete, name="patient_delete"),
    ]


