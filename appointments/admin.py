from django.contrib import admin
from .models import Appointment


class AppointmentModelAdmin(admin.ModelAdmin):
	list_display = ["name", "date", "user"]
	#list_editable = ["title"]
	list_filter = ["date", "user"]
	#search_fields = ["user"]
	class Meta:
		model = Appointment


# Register your models here.
admin.site.register(Appointment,AppointmentModelAdmin)

