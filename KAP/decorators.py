from django.http import HttpResponseRedirect
from django.urls import reverse


def user_check(view_func):
    def wrap(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrap


def doctor_check(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles=["Admin", "Doctor"]
        if request.role in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('patient_list'))
    return wrap


def admin_check(view_func):
    def wrap(request, *args, **kwargs):
        if request.role == "Admin":
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('patient_list'))
    return wrap

