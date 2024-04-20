from django.db import models

from trainer.models import Trainer


class Module(models.Model):
    name = models.CharField(max_length=40)
    trainer = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

