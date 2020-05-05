from django import forms
from models import Webpage
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vmail = all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email doesn't match!")