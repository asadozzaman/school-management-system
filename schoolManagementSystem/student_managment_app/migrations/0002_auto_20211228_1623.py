# Generated by Django 3.2.9 on 2021-12-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_managment_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='teacher_name',
        ),
        migrations.AlterField(
            model_name='class',
            name='class_numeric',
            field=models.IntegerField(),
        ),
    ]