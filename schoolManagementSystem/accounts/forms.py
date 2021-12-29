from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Admin,Student, User, Teacher,Headmaster,Parent


class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        return user


class HeadmasterSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_headmaster = True
        user.save()
        headmaster = Headmaster.objects.create(user=user)
        headmaster.phone = self.cleaned_data.get('phone')
        headmaster.save()

        return headmaster

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.phone = self.cleaned_data.get('phone')
        teacher.save()

        return teacher

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.phone = self.cleaned_data.get('phone')
        student.save()

        return student

class ParentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        parent = Parent.objects.create(user=user)
        parent.phone = self.cleaned_data.get('phone')
        parent.save()

        return parent