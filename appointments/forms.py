from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "title",
            "date",
            "comment",
        ]
    first_name = forms.DateTimeInput()# TextInput(attrs={'id': 'firstname',  'class':'form-control'})
    """
    title = forms.CharField(label='Titel', max_length=50)
    date = forms.DateTimeInput()
    comment = forms.CharField(label='Kommentar',max_length=200)
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)	
    title = models.CharField(max_length=50)
    date = models.DateTimeField('Termin')
    comment = models.CharField(max_length=200)
    files = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    """