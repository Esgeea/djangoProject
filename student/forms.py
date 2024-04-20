from django import forms
from django.forms import TextInput, EmailInput, Textarea, Select, NumberInput, DateInput

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #exclude =['first_name'] # TREBUIE CA IN MODELS.PY SA AVETI BLANK=TRUE SI NULL=TRUE
        fields = '__all__'  # specificam ce fields sunt luate din formular, all - toate
        # fields = ['first_name', 'last_name']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter a description', 'class': 'form-control', 'rows': 3}),
            'gender': Select(attrs={'class': 'form-select'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})
        }


    # Atunci cand creati sau personalizati un formular in Django puteti sa implementati validari personalizate
    # care se va aplica pe intregul formular

    # Aceasta metoda este folosita pentru a verifica corectitudinea datelor introduse de utilizator
    # inainte de fi procesate sau salve in baza de date


    def clean(self):
        cleaned_data = super().clean() # se obtine access la informatiile din formular intr-un dictionar
        print(cleaned_data)

        # o unicitate pe adresa de email
        get_email = cleaned_data['email']

        #Varianta 1
        check_emails = Student.objects.filter(email=get_email)
        if check_emails:
            msg = 'Email already exists in database!'
            self._errors['email'] = self.error_class([msg])


        #Varianta 2
        #all_students = Student.objects.all()
        #for student in all_students:
        #    if student.email == get_email:
        #        print('Exista deja')


        # o unicitate pe first_name, respectiv last_name
        get_first_name = cleaned_data['first_name']
        get_last_name = cleaned_data['last_name']
        check_name = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)

        if check_name:
            msg = 'The student with this first name and last name already exists!'
            self._errors['first_name'] = self.error_class([msg])
            self._errors['last_name'] = self.error_class([msg])


        # o validare pe campul description in care utilizatorul TREBUIE sa introduca minim 10 caractere
        get_description = cleaned_data['description']
        check_description = len(get_description) < 10
        if check_description:
            msg = 'You must enter more than 10 characters!'
            self.errors['description'] = self.error_class([msg])


        # o validare pe campurile start_date si end_date. Daca start_Date este mai mare decat end_date sa se genereze o eroare in interfata
        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']
        check_dates = get_end_date < get_start_date
        if check_dates:
            msg = 'End date should be after start date!'
            self.errors['end_date'] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter a description', 'class': 'form-control', 'rows': 3}),
            'gender': Select(attrs={'class': 'form-select'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})
        }
