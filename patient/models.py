from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PatientProfile(models.Model):
    id_code = models.CharField(max_length=20, null=False, blank=False)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
