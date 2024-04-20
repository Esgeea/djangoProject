from django.contrib.auth.models import User
from django.db import models
from django.forms import BooleanField

from trainer.models import Trainer

gender_options = (
    ('male', 'Male'),   # prima este pentru stocare in baza si a doua pentru afisare
    ('female', 'Female')
)


class Student(models.Model):
    first_name = models.CharField(max_length=40)  # 255 e max permis, daca se pune mai mult de atat, in tabela se stocheaza tot pana la 255
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(blank=True, null=True)  # blank=true -> fieldul nu e cerut obligatoriu
    email = models.EmailField()
    description = models.TextField(max_length=500)  # permite numar nelimitat de caractere, este indicat sa se limiteze totusi cu un max_length
    active = models.BooleanField(default=True)  # checkbox in interfata
    gender = models.CharField(max_length=6, choices=gender_options)
    start_date = models.DateField()
    end_date = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='students/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auto_now_add=True -> stocheaza data si ora cand a fost adaugata inregistrarea, fara modificari ulterioare
    # auto_now=True -> stocheaza data si ora de fiecare data cand se realizeaza modificari pe inregistrare

    def __str__(self):  # reprezentare obiect sub forma de string
        return f'{self.first_name} {self.last_name}'


class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message
