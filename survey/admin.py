from django.contrib import admin
from survey.models import *

# Register your models here.
admin.site.register(TextQuestion)
admin.site.register(TextChoice)
admin.site.register(TextAnswer)
