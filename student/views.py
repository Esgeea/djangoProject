from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent


# CreateView -> este o clasa dezvoltata de Django care ajuta la definirea unui obiect in baza de date
# si la afisarea unui formular asociat modelului definit in models.py

# Caracteristici:
# - formular de create: automat se genereaza un formular asociat modelului pentru a adauga un obiect in db
# - procesarea datelor: gestionarea si procesarea detelor introduse in formular prin validare
# - redirectionare dupa creare: in momentul in care obiectul este creat cu success, utilizatorul poate fi redirectionat pe o pagina dorita


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    template_name = 'student/create_student.html'  # randare template dorit in care se va regasi formularul
    model = Student  # modelul asociat formularului, clasa Student creata in models.py file
    form_class = StudentForm
    success_url = reverse_lazy('list-students')  # url de redirectionare daca rularea este facuta cu success, reverse_lazy foloseste name-ul ales de la aplicatie, fisierul de urls
    permission_required = 'student.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=True)

            history = f'A fost adaugat un nou student cu numele {new_student}'
            HistoryStudent.objects.create(message=history, created_at=datetime.now(), active=True,
                                          user=User.objects.get(id=self.request.user.id))

        return redirect('list-students')

# ListView -> este o clasa dezvoltata de Django care va ajuta pentru a afisa o lista de obiecte dintr-un model
# specificat in template (.html)

# Caracteristici:

# - automatizeaza procesul de preluare a listei de obiecte dintr-un model
# - ListView foloseste un sablon implicit dar va lasa sa il folisiti pe al vostru


class StudentListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students' # Student.objects.all()
    permission_required = 'student.view_list_of_students'

    # Metoda get_queryset este un element cheie in clase de view bazate pe ListView in Django, permitand
    # personalizarea setului de obiecte care sunt recuperate din baza de date si afisate in template.

    #Acesta metoda oferta flexibilitatea de a filtra, ordona sau limita datele pe care doriti sa le prezentati
    # utilizatorilor, in functie de logica specificata aplicatiei sau de cerinte de business

    def get_queryset(self):
        return Student.objects.filter(active=True)


    # metoda folosita in clasele de views - list/update/create/etc.
    # folosita pentru a obtine si pregati datele pentru a fi afisate in template
    # metoda este utilizata pentru a furniza contextul necessar pentru template pentru a afisa corect informatiile
    # cand este apelata metoda, se obtine un dictionar de date pe care il trimitem in template
    # programatorii pot suplimenta cu informatii noi acel dictionar
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        students = Student.objects.filter(active=True)
        myFilter = StudentFilter(self.request.GET, queryset=students)
        students = myFilter.qs
        data['all_students'] = students
        data['filters'] = myFilter.form

        return data


@login_required()
def get_all_students_per_trainer(request, pk):
    students_per_trainer = Student.objects.filter(trainer_id=pk) # Realizam un query prin care accesam toti studentii alocati trainerului selectat

    return render(request, 'student/list_of_students.html', {'all_students': students_per_trainer})


# UpdateView - clasa generica din Django, ce simplifica procesul de actualizare a inregistrarilor din db
# pe baza unui formular de date

# Caracteristici:
# - automatizeaza multe din sarcinile asociate cu preluarea unui obiect dintr-o db, afisarea unui formular populat
# cu datele obiecctului, validarea datelor trimise prin formular si salvarea acestuia
# - utilizeaza un formular pentru a afisa datele si a le valida

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-students')


# DeleteView - clasa generica in Django utilizata pentru stergerea unei inregistrari din baza de date
class StudentDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-students')


# DetailView - clasa generica in Django utilizata pentru a afisa detaliile unei inregistrari din baza de date
class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student


class HistoryStudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/history_student.html'
    model = HistoryStudent
    context_object_name = 'history_student'

    def get_queryset(self):
        user = self.request.user
        return HistoryStudent.objects.filter(user=user)







