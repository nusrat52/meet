from django import forms

class RegistrationForm(forms.Form):
    email=forms.EmailField(label="Email field")