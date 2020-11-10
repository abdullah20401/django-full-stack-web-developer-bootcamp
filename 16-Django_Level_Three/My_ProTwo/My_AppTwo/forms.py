from django import forms
from My_AppTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'