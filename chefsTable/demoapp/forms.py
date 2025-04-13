from django import forms
from .models import Logger

class LoggerForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = ['first_name', 'last_name', 'log_time']
        widgets = {
            'log_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

SHIFTS = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
)

class InputForms(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    shift = forms.ChoiceField(label='Shift', choices=SHIFTS)
    time_logged = forms.DateTimeField(label='Time Logged')
    
    
    # Add any other fields you need for the Drinks model


