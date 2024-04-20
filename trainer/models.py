from django.db import models

department_options = (
    ('backend', 'Backend'),
    ('frontend', 'Frontend'),
    ('network', 'Network')
)

class Trainer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=8, choices=department_options)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    profile = models.ImageField(upload_to='trainers/', null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

