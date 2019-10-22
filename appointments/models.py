from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL
# Create your models here.

class Appointment(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)	
	name = models.CharField(max_length=50)
	date = models.DateTimeField('Termin')
	comment = models.CharField(max_length=200)
	files = models.PositiveIntegerField()
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("appointments:detail",kwargs={"id": self.id})
        #return "/appointments/detail/%s" %(self.id)