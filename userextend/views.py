from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import UserHistory


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


    # form_valid este o metoda in clase de view si este apelata atunci cand formularul este trimis si
    # programatorul poate sa suplimenteze cu actiuni noi

    def form_valid(self, form):

        # Customizarea first_name si last_name pentru a le salva sub forma unui title()
        new_user = form.save(commit=False)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.last_name.title()
        # Atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user


        # Generarea unui username

        new_user.username = f"{new_user.first_name[0].lower()}{new_user.last_name.replace(' ', '').lower()}_{randint(100000, 999999)}"
        new_user.save()

        # Trimite mail FARA TEMPLATE
        subject = 'Cont nou in DjangoProject'
        message = (f'Buna ziua, {new_user.first_name} {new_user.last_name}. Contul tau a fost adaugat cu succes. Pentru autentificare vei avea'
                   f'nevoie de numele de utilizator: {new_user.username}. Te asteptam cu mult drag!')

        #send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

        # Trimitere mail CU TEMPLATE
        details_user = {
            'fullname': f"{new_user.first_name} {new_user.last_name}",
            'username': f'{new_user.username}'
        }
        subject = 'Cont nou in DjangoProject'
        message = get_template('mail.html').render(details_user)

        mail = EmailMessage(
            subject,
            message,
            EMAIL_HOST_USER,
            [new_user.email]
        )
        mail.content_subtype = 'html'
        # mail.send()

        # Implementare istoric
        history = f'A fost adaugat urmatorul user: first_name: {new_user.first_name}, last_name: {new_user.last_name}, email: {new_user.email}'
        UserHistory.objects.create(text=history)

        return redirect('login')