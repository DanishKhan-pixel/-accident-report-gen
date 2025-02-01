from django import forms
from .models import ViolationReport

class ViolationReportForm(forms.ModelForm):
    class Meta:
        model = ViolationReport
        fields = ['date', 'time', 'location', 'license_plate', 'distance', 'speed', 'gps', 'observations', 'photo']
