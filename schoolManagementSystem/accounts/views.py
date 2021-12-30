from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import CreateView

from .forms import AdminSignUpForm, TeacherSignUpForm, HeadmasterSignUpForm, StudentSignUpForm , ParentSignUpForm
from .models import User


# Create your views here.

def frontpage(request):
    return render(request,"frontpage.html")


def SingUp(request):
    return render(request, 'register.html')


class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('singup')


class HeadmasterSignUpView(CreateView):
    model = User
    form_class = HeadmasterSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'headmaster'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('singup')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('singup')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('singup')

class ParentSignUpView(CreateView):
    model = User
    form_class = ParentSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('singup')

@login_required
def profilepage(request):
    return render(request, 'profile.html')


@login_required
def student(request):
    return render(request, 'student.html')
@login_required

def admin(request):
    return render(request, 'admin.html')

@login_required
def headmaster(request):
    return render(request, 'headmaster.html')

@login_required
def teacher(request):
    return render(request, 'teacher.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('rrrrrrr')
            if user.is_authenticated and user.is_admin:
                print('adminnnnnnn')
                return redirect('student_managment_app:classShow')  # Go to student home
            elif user.is_authenticated and user.is_headmaster:
                return redirect('student_managment_app:classShow')  # Go to teacher home
            elif user.is_authenticated and user.is_teacher:
                return redirect('student_managment_app:sectionShow')  # Go to teacher home
            elif user.is_authenticated and user.is_student:
                return redirect('student_managment_app:classShow')  # Go to teacher home
        else:
            print('tttttt')
            return redirect('singup')

    return render(request, 'login.html')

    # if (request.method == 'post'):
    #     username = request.POST.get('username')  # Get email value from form
    #     password = request.POST.get('password')  # Get password value from form
    #     user = authenticate(request, username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         if user.is_authenticated and user.is_doctor:
    #             return redirect('profile')  # Go to student home
    #         elif user.is_authenticated and user.is_teacher:
    #             return redirect('profile')  # Go to teacher home
    #     else:
    #         # Invalid email or password. Handle as you wish
    #         return redirect('login')
    #
    # return render(request, 'login.html')
