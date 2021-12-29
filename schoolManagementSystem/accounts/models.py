from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_headmaster = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
    	return self.user.username



class Headmaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)

    def __str__(self):
    	return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)

    def __str__(self):
    	return self.user.username + ' -- ' + self.phone

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)

    def __str__(self):
    	return self.user.username + ' -- ' + self.phone

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)

    def __str__(self):
    	return self.user.username + ' -- ' + self.phone