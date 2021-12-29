from django.urls import path
from .views import SingUp,AdminSignUpView,TeacherSignUpView,HeadmasterSignUpView,StudentSignUpView,ParentSignUpView,profilepage,student,teacher,user_login,admin,headmaster
from django.contrib.auth import views as authentication_views


urlpatterns = [
  path('singup/',SingUp,name='singup'),
  path('accounts/signup/admin/', AdminSignUpView.as_view(), name='admin_signup'),
  path('accounts/signup/headmaster/', HeadmasterSignUpView.as_view(), name='headmaster_signup'),
  path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
  path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
  path('accounts/signup/parent/', ParentSignUpView.as_view(), name='parent_signup'),
  path('profile/',profilepage,name='profile'),
  path('admin/',admin,name='admin'),
  path('headmaster/',headmaster,name='headmaster'),
  path('student/',student,name='student'),
  path('teacher/',teacher,name='teacher'),
  path('logout/', authentication_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
  path('login/', user_login, name='login'),

]