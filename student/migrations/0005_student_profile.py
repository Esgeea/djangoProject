# Generated by Django 5.0.3 on 2024-03-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(null=True, upload_to='students/'),
        ),
    ]
