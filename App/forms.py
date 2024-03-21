# forms.py

from django import forms
from .models import Contact, donor, login

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'desc']

class DonorForm(forms.ModelForm):
    class Meta:
        model = donor
        fields = ['name', 'product', 'mobile', 'location', 'quantity', 'about_product']

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Username', 'password']
