from django.shortcuts import render,redirect    
from django.http import HttpResponse    
from .models import Employee,Department
from django.contrib import messages

def dbprocessing(request):
    return  HttpResponse("DB processing done")  
def insertemployee(request):
    if request.method=="GET":
        dep=Department.objects.all()
        return render(request,'DBapp/insert.html',{'departments':dep})
    if request.method=="POST":
        empno=int(request.POST['empno'])
        ename=request.POST['ename']
        salary=int(request.POST['salary'])
        ddno = int(request.POST['dno'])
        epic=request.FILES['epic']
        evideo=request.FILES['evideo']
        ebj = Department.objects.get(deptno=ddno)
        eobj=Employee.objects.create(empno=empno,ename=ename,salary=salary,dept=ebj,profile_pic=epic,video=evideo)
        messages.success(request,"Employee inserted successfully")
        return redirect('selecturl')
       
def selectemployee(request):
    if request.method=="GET":
        # select * from employee
        emps=Employee.objects.all()
        return render(request,'DBapp/select.html',{'employees':emps})
def updateemployee(request,empno):
    if request.method=='GET':
        # selet * from employee where empno=empno
        eobj=Employee.objects.get(empno=empno)
        return render(request,'DBapp/update.html',{'employee':eobj})
    if request.method=='POST':
        ename=request.POST.get('ename','')
        salary=int(request.POST.get('salary','0'))
        eobj=Employee(empno=empno
                  ,ename=ename,salary=salary)
        eobj.save()
        messages.success(request,"Employee updated successfully")
        return redirect ('selecturl')
def deleteemployee(request,empno):
    if request.method=='GET':
        eobj=Employee.objects.get(empno=empno)
        return render(request,'DBapp/delete.html',{'employee':eobj})  
    if request.method=='POST':
        eobj=Employee.objects.get(empno=empno)
        eobj.delete()
        return redirect('selecturl')



# Create your views here.
