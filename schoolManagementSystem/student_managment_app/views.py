from django.shortcuts import render,redirect
from student_managment_app.models import MyClassName
from student_managment_app.forms import MyClassNameForm
from django.contrib import messages

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.
# def showDemoPage(request):
#     return render(request,"demo.html")

def allRegister(request):
    return render(request,"register.html")


def frontpage(request):
    return render(request,"frontpage.html")



def showDemoPage(request):
    MyClassNames=MyClassName.objects.all()
    # staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"admin/class/index.html",{"MyClassNames":MyClassNames})

# def classAdd(request):
#     return render(request,"add.html")

def classAdd(request):
    if request.method == "POST":
        form = MyClassNameForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('student_managment_app:classShow')
            except:
                pass
    else:
        form = MyClassNameForm()
    return render(request,'admin/class/add.html',{'form':form})


# def edit(request, id):
#     MyClassNames = MyClassName.objects.get(id=id)
#     return render(request,'edit.html', {'MyClassNames':MyClassNames})



def edit(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(MyClassName, id=id)

    # pass the object as instance in form
    form = MyClassNameForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request,"Class Added Successfully")
        return redirect('student_managment_app:classShow')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/class/edit.html", context)


# def update(request, id):
#     context = {}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(MyClassName, id=id)
#
#     # pass the object as instance in form
#     form = MyClassNameForm(request.POST or None, instance=obj)
#
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/" + id)
#
#     # add form dictionary to context
#     context["form"] = form
#     return render(request, "update_view.html", context)


def destroy(request, id):
    MyClassNames = MyClassName.objects.get(id=id)
    MyClassNames.delete()
    messages.success(request, "Class Added Successfully")
    return redirect('student_managment_app:classShow')