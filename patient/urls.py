from django.urls import path
from patient.views import *

urlpatterns = [
    path('', patient_list, name='list'),
    path('<int:id>/details/', patient_details, name="details"),
    path('<int:id>/edit/', patient_edit, name="edit"),
    path('add/', patient_add, name="add"),
    path('<int:id>/delete/', patient_delete, name="delete"),
    ]


