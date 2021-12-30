from django.db import models
from accounts.models import User,Student,Teacher,Admin,Headmaster,Parent

# Create your models here.

class MyClassName(models.Model):
    id=models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
    class_numeric = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class SectionName(models.Model):
    id = models.AutoField(primary_key = True)
    section_name = models.CharField(max_length=255)
    class_name_id = models.ForeignKey(MyClassName, on_delete=models.DO_NOTHING)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class SubjectName(models.Model):
   id = models.AutoField(primary_key = True)
   subject_name = models.CharField(max_length=255)
   class_name_id = models.ForeignKey(MyClassName, on_delete=models.DO_NOTHING)
   section_name_id = models.ForeignKey(SectionName, on_delete=models.DO_NOTHING)
   teacher_name_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
   subject_type = [
       ('mandatory', 'mandatory'),
       ('optional', 'optional'),
   ]
   full_marks = models.IntegerField()
   pass_marks = models.IntegerField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
