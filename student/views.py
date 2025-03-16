
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here

def homepage(request):
    students = (Student.objects.all())
    context = {'students':students}
    return render(request,'index.html',context)

def add_student(request):
    if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request,messages.SUCCESS,'Student added successfully')
         return redirect('studentlist')
    else:
        form = StudentForm()
        return render(request,'add_student.html',{'form':form})
    

def delete_student(request,student_id):
   student=Student.objects.get(id=student_id)
   if student:
      student.delete()
      messages.add_message(request,messages.INFO,'Record Deleted')
      return redirect('studentlist')
   

def update_student(request,student_id):
    specific_student=Student.objects.get(id=student_id)
    if request.method == 'POST':
      form = StudentForm(request.POST,instance=specific_student)
      if form.is_valid():
         form.save()
         messages.add_message(request,messages.WARNING,'Record Updated')
         return redirect('studentlist')
    else:
        form = StudentForm(instance=specific_student)
        return render(request,'add_student.html',{'form':form})


def studentlist(request):
    students = (Student.objects.all())
    context = {'students':students}
    return render(request,'studentlist.html',context)