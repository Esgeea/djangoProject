import django_filters
from django import forms

from student.models import Student
from trainer.models import Trainer

#lookup_exp - icontains, exact, startswith, endswith, lte, lt, gte, gt

#lte -> less than or egual to
#lt -> less than

#gte -> greater than or equal to
#gt -> greater than

class StudentFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label ='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label ='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter last name'}))
    age = django_filters.NumberFilter(label='Age', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter age'}))

    start_date_gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', widget=forms.DateInput(attrs={'class': 'form-control','type': 'date' }))
    start_date_lte = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', widget=forms.DateInput(attrs={'class': 'form-control','type': 'date' }))

    end_date_gte = django_filters.DateFilter(field_name='end_date', lookup_expr='gte',
                                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date_lte = django_filters.DateFilter(field_name='end_date', lookup_expr='lte',
                                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    trainer = django_filters.ChoiceFilter(widget=forms.RadioSelect(), choices=[(trainer.id, trainer) for trainer in Trainer.objects.filter(active=True)])

    email = django_filters.CharFilter(lookup_expr='icontains', label = 'Email' , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter email'}) )


    # Varianta 1
    #course = django_filters.CharFilter(field_name='trainer__course', method='filter_by_course', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter course'}))

    #def filter_by_course(self, queryset,name,  value):
    #    return queryset.filter(trainer__course=value)

    #Varianta 2
    list_options = []
    for trainer in Trainer.objects.filter(active=True):
        if (trainer.course, trainer.course) not in list_options:
            list_options.append((trainer.course, trainer.course))
    # print(list_options, '?')

    # course_options = [(trainer.course, trainer.course) for trainer in Trainer.objects.filter(active=True)]   # va afisa si duplicates
    course = django_filters.ChoiceFilter(label='Course', field_name='trainer__course', choices = list_options, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'start_date_gte', 'start_date_lte', 'end_date_gte','end_date_lte', 'trainer', 'email']