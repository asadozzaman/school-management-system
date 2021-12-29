from django.db import models
from accounts.models import User,Student,Teacher,Admin,Headmaster,Parent

# Create your models here.

class MyClassName(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    class_name = models.CharField(max_length=255)
    class_numeric = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
