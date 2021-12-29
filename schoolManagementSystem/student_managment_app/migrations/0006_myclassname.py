# Generated by Django 3.2.9 on 2021-12-28 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('student_managment_app', '0005_delete_classname'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClassName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=255)),
                ('class_numeric', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.teacher')),
            ],
        ),
    ]