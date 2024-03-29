from django import forms
from .models import Citizen, Certificate, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = "__all__"
        exclude = ("slug", )

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = ("user", )


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date' 
            #,'profile_image'
        ]