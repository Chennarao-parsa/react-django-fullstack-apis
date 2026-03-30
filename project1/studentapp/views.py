from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse


def add_student(request):
    if request.method == "GET":
       return render(request, 'studentapp/add_student.html')
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        course = request.POST['course']
        Student.objects.create(name=name, age=age, course=course)
        return redirect('list_students')
    

    
def list_students(request):
    students = Student.objects.all()
    return render(request, 'studentapp/list_students.html', {"students": students})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list_students')
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('list_students')

    return render(request, 'studentapp/update_student.html', {"student": student})

# Create your views here.
