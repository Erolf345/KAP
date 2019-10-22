from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.appointment_list, name='list'),
    path('create/', views.appointment_create, name='create'),
    path('detail/<int:id>/', views.appointment_detail, name='detail'),
    path('list/', views.appointment_list, name='list'),
    path('edit/<int:id>/', views.appointment_edit, name='edit'),
    path('delete/<int:id>/', views.appointment_delete, name='delete'),
]