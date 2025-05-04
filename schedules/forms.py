from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'  # or list specific fields, e.g. ['title', 'date']
