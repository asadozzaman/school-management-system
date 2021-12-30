from django import forms
from student_managment_app.models import *



# creating a form
class MyClassNameForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = MyClassName

        # specify fields to be used
        fields = [
            "class_name",
            "class_numeric",
        ]
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_numeric': forms.TextInput(attrs={'class': 'form-control'}),
            }

class SectionNameForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = SectionName

        # specify fields to be used
        fields = [
            "section_name",
            "class_name_id",
            "capacity",
        ]
        widgets = {
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name_id': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control'}),
            }


