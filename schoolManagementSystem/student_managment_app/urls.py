from django.urls import path
from student_managment_app.views import  *

app_name = 'student_managment_app'

urlpatterns = [
    # Class name url
    path('classShow', showDemoPage, name='classShow'),
    path('classAdd', classAdd, name='classAdd'),
    path('allRegister',allRegister, name='allRegister'),
    path('edit/<int:id>',edit, name= 'edit'),
    path('delete/<int:id>', destroy),

]