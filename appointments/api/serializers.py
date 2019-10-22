from rest_framework import serializers, viewsets
from appointments.models import Appointment
from django.contrib.auth.models import User

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ('name','date','comment','files')