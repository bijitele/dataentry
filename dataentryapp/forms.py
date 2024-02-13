from django import forms
from .models import Citizen, Certificate

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = "__all__"  

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = ("user", )
