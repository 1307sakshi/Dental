# forms.py
from django import forms
from appoint.models import Appointment,app

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'time', 'message']




class CheckoutForm(forms.ModelForm):
    class Meta:
        model = app
        fields = ['preferred_date', 'message']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }