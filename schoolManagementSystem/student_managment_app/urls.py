from django.urls import path
from student_managment_app.views import  *
from student_managment_app.admin_views import  *

app_name = 'student_managment_app'

urlpatterns = [
    # Class name url
    path('classShow', showDemoPage, name='classShow'),
    path('classAdd', classAdd, name='classAdd'),
    path('edit/<int:id>',edit, name= 'edit'),
    path('delete/<int:id>', destroy),

    # Section name url
    path('sectionShow', sectionShowView, name='sectionShow'),
    path('sectionAdd', sectionAddView, name='sectionAdd'),
    path('sectionEdit/<int:id>', sectionEditView, name='sectionEdit'),
    path('sectionDelete/<int:id>', sectionDeleteView,name='sectionDelete'),

    # Subject name url
    path('subjectShow', subjectShowView, name='subjectShow'),
    path('subjectAdd', subjectAddView, name='subjectAdd'),
    path('subjectEdit/<int:id>', subjectEditView, name='subjectEdit'),
    path('subjectDelete/<int:id>', subjectDeleteView,name='subjectDelete'),

    path('logout_user', logout_user, name="logout"),

]