from django import forms
from student_managment_app.models import MyClassName


class MyClassNameForm(forms.ModelForm):
    class Meta:
        model = MyClassName
        fields = "__all__"


# creating a form
class MyClassNameForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = MyClassName

        # specify fields to be used
        fields = [
            "teacher_id",
            "class_name",
            "class_numeric",
        ]
        widgets = {
            'teacher_id': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_numeric': forms.TextInput(attrs={'class': 'form-control'}),
            }