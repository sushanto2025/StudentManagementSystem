from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('add_student/',views.add_student,name='add_student'),
    path('delete/<int:student_id>/',views.delete_student,name='delete_student'),
    path('update/<int:student_id>/', views.update_student,name='update_student'),
    path('list/',views.studentlist,name='studentlist')
]
