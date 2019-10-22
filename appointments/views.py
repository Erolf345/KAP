from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Appointment

def appointment_create(request):
    if request.user.is_authenticated:
        context = {
        "content": "Hello " + str(request.user.username),
        }
        return render(request,"appointments/index.html",context)
    else:
        return HttpResponse("<h1>Please login ")
    
def appointment_detail(request,id=None):
    instance = get_object_or_404(Appointment,id=id)
    context = {
        "content": str(instance.name)
    }
    return render(request,"appointments/details.html",context)

def appointment_list(request):
    queryset = Appointment.objects.all()
    context = {
        "appointments": queryset,
        "content": "List"
    }
    return render(request,"appointments/index.html",context)

def appointment_update(request):
    return HttpResponse("<h1>Update</h1>")

def appointment_delete(request):
    return HttpResponse("<h1>Delete</h1>")