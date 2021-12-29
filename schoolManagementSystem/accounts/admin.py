
from django.contrib import admin

# Register your models here.
from accounts.models import User,Student,Teacher,Admin,Headmaster,Parent


admin.site.register(User)

admin.site.register(Admin)

admin.site.register(Headmaster)

admin.site.register(Student)

admin.site.register(Teacher)

admin.site.register(Parent)

