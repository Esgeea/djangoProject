import django_filters
from django import forms

from trainer.models import Trainer, department_options


class TrainerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter last name'}))
    course = django_filters.CharFilter(lookup_expr='icontains', label='Course', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter course'}))
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter email'}))

    departament = django_filters.ChoiceFilter(label='Department', field_name='department', choices=department_options, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email']