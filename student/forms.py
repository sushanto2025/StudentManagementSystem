from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','phonenumber','course']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control'
            }),
            'phonenumber' : forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'course' : forms.TextInput(attrs={
                'class':'form-control'
            }),
        }