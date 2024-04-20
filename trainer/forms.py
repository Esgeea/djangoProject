from django import forms
from django.forms import TextInput, EmailInput, Select

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            'first_name': TextInput(attrs={'placeholder':'Add the first name for trainer', 'class':'form-control'}),
            'last_name': TextInput(attrs={'placeholder':'Add the last name for trainer', 'class':'form-control'}),
            'course': TextInput(attrs={'placeholder':'Add the course', 'class':'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-select'}),

        }

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Add the first name for trainer', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Add the last name for trainer', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Add the course', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-select'}),
        }