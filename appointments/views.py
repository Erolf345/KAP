from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Appointment
from .forms import AppointmentForm

def removeSensitiveAppointment(request, appointment):
    print(request.user)
    print(appointment.user)
    if request.user != appointment.user:
            appointment.user = None
            appointment.title = None
            appointment.comment = None
            appointment.files = 0
            appointment.timestamp = None
            appointment.id = 0

def removeSensitiveData(request,queryset):
    for appointment in queryset:
        removeSensitiveAppointment(request, appointment)

@login_required(login_url="/login/")
def appointment_create(request):
    if request.user.is_authenticated:
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        
        context = {
        "form": form,
        }
        return render(request,"appointments/add.html",context)
    else:
        return HttpResponse("<h1>Bitte loggen sie sich zuerst ein</h1>")

@login_required(login_url="/login/")
def appointment_detail(request,id=None):
    instance = get_object_or_404(Appointment,id=id)
    if request.user != instance.user:
        return HttpResponse('<h1>Unauthorized</h1>', status=401)
    context = {
        "content": str(instance.title)
    }
    return render(request,"appointments/details.html",context)

@login_required(login_url="/login/")
def appointment_list(request):
    queryset = Appointment.objects.all()
    removeSensitiveData(request,queryset)
    context = {
        "title":"Appointments",
        "appointments": queryset,
    }
    return render(request,"appointments/index.html",context)

@login_required(login_url="/login/")
def appointment_edit(request, id=None):
    instance = get_object_or_404(Appointment,id=id)
    if request.user != instance.user:
        return HttpResponse('<h1>Unauthorized</h1>', status=401)
    context = {
        "content": str(instance.title)
    }
    return render(request,"appointments/details.html",context)

@login_required(login_url="/login/")
def appointment_delete(request, id=None):
    instance = get_object_or_404(Appointment,id=id)
    if request.user != instance.user:
        return HttpResponse('<h1>Unauthorized</h1>', status=401)
    return HttpResponse("<h1>Delete</h1>")