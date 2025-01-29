from django import forms
from django.forms import ModelForm
from .models import Emails

class EmailForm(ModelForm):
    email = forms.EmailField(label='Email', required=True)
    
    class Meta:
        model = Emails
        exclude = ['created_at', 'edited_at', 'message', 'subject']