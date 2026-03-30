from django.shortcuts import render
def calculate(request):
    if request.method == 'GET':
        return render(request,'calculatoradd.html')
    if request.method == 'POST':
        num1=float(request.POST.get('num1','0'))
        num2=float(request.POST.get('num2','0'))
        op=request.POST.get('operation','add')
        result=0
        if op=='add':
            result=num1+num2
        elif op=='sub':
            result=num1 - num2
        elif op=='mul':
            result=num1 * num2
        elif op=='div':
            if num2 != 0:
                result=num1 / num2
            else:
                result='Error: Division by zero'
        else:
            result='Invalid operation'
        return render(request,'calculatoradd.html',{'result':result})            
# Create your views here.
