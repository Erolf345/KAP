from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from patient.forms import UserForm
from KAP.decorators import admin_check, doctor_check, user_check

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('patient:list'))
        else:
            context['error'] = "Provide valid credentials"
            return render(request, "auth/login.html", context)
    else:
         return render(request, "auth/login.html", context)


@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url="/login/")
def patient_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Patients'
    return render(request, 'patient/index.html', context)


@login_required(login_url="/login/")
def patient_details(request, id=None):
    context = {}
    context['users'] = get_object_or_404(User, id=id)
    context['title'] = 'Patients'
    return render(request, 'patient/details.html', context)


@login_required(login_url="/login/")
@doctor_check
def patient_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('patient:list'))
        else:
            return render(request, 'patient/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'patient/add.html', context)


@login_required(login_url="/login/")
def patient_edit(request, id=None):
    context = {}
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('patient:list'))
        else:
            return render(request, 'patient/edit.html', context)
    else:
        user_form = UserForm(instance=user)
        context['user_form'] = user_form
        return render(request, 'patient/edit.html', context)


@login_required(login_url="/login/")
@doctor_check
def patient_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse('patient:list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'patient/delete.html', context)