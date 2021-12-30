from django.shortcuts import render,redirect
from student_managment_app.models import MyClassName,SectionName
from student_managment_app.forms import SectionNameForm
from django.contrib import messages

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.

def sectionShowView(request):
    sectionNames=SectionName.objects.all()
    # staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"admin/section/index.html",{"sectionNames":sectionNames})

def sectionAddView(request):
    if request.method == "POST":
        form = SectionNameForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('student_managment_app:sectionShow')
            except:
                pass
    else:
        MyClassNames = MyClassName.objects.all()
        form = SectionNameForm()
    return render(request,'admin/section/add.html',{'form':form,"MyClassNames":MyClassNames})

def sectionEditView(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(SectionName, id=id)

    # pass the object as instance in form
    form = SectionNameForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request,"Section Added Successfully")
        return redirect('student_managment_app:sectionShow')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/section/edit.html", context)


def sectionDeleteView(request, id):
    sectionNames = SectionName.objects.get(id=id)
    sectionNames.delete()
    messages.success(request, "Section Added Successfully")
    return redirect('student_managment_app:sectionShow')



# subject crud



def subjectShowView(request):
    sectionNames=SectionName.objects.all()
    # staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"admin/subject/index.html",{"sectionNames":sectionNames})

def subjectAddView(request):
    if request.method == "POST":
        form = SectionNameForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('student_managment_app:sectionShow')
            except:
                pass
    else:
        MyClassNames = MyClassName.objects.all()
        form = SectionNameForm()
    return render(request,'admin/subject/add.html',{'form':form,"MyClassNames":MyClassNames})

def subjectEditView(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(SectionName, id=id)

    # pass the object as instance in form
    form = SectionNameForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request,"Section Added Successfully")
        return redirect('student_managment_app:sectionShow')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/section/edit.html", context)


def subjectDeleteView(request, id):
    sectionNames = SectionName.objects.get(id=id)
    sectionNames.delete()
    messages.success(request, "Section Added Successfully")
    return redirect('student_managment_app:sectionShow')
