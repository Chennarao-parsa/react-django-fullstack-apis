from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addition(request):
    result=None
    if request.method == 'GET':
        return  render (request,'calculator/addition.html')
    if request.method == "POST":
        v1=int(request.POST.get('t1',0))
        v2=int(request.POST.get('t2',0))
        operation=request.POST.get('operation')
        if (operation=='add'):
            result=v1+v2
        elif operation == 'sub':
            result=v1-v2
        elif operation == 'mul':
            result=v1*v2
        elif operation=='div':
             if v2 != 0:
                result = v1 / v2
             else:
                result = "Cannot divide by zero!"

    return render(request, "calculator/addition.html", {"result": result})
def calculator(request):
    res = None  # always define before
    if request.method == 'GET':
        return  render (request,'calculator/calculator.html')
    

    if request.method == 'POST':
        v1 = float(request.POST.get('t1', 0))
        v2 = float(request.POST.get('t2', 0))

        if 'add' in request.POST:
            res = v1 + v2
            action='Addition'
        elif 'sub' in request.POST:
            res = v1 - v2
            action="Substraction"
        elif 'mul' in request.POST:
            res = v1 * v2
            action='Multiplication'
        elif 'div' in request.POST:
            res = v2/v1
            action='Division'

        return render(request, 'calculator/calculator.html', {'result': res,'action':action})
def generatetable(request):
    if request.method=='GET':
        return render(request,'calculator/mtable.html')
    if request.method == "POST":
        num = int(request.POST.get('t1',0))
        output=[]
        for  i in range(1,11):
            output.append(str(num)+' * '+str(i)+' = '+str(i*num))
        return render(request,'calculator/mtable.html',{'result':output})
    

    
