# Generated by Django 5.0.3 on 2024-03-10 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_age'),
        ('trainer', '0002_alter_trainer_created_at_alter_trainer_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.trainer'),
        ),
    ]
