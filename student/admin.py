from django.contrib import admin

from module.models import Module
from student.models import Student
from trainer.models import Trainer

admin.site.register(Student)
admin.site.register(Trainer)
admin.site.register(Module)