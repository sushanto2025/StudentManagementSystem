from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','phonenumber','course']
        widget = {
            'name' : forms.TextInput(),
            'email': forms.EmailInput(attrs={
                'type':'email'
            }),
            'phonenumber' : forms.NumberInput(attrs={
                'type':'number'
            })
        }