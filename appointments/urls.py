from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.appointment_list),
    path('create/', views.appointment_create),
    path('detail/<int:id>/', views.appointment_detail, name='detail'),
    path('list/', views.appointment_list),
    path('update/', views.appointment_update),
    path('delete/', views.appointment_delete),
]