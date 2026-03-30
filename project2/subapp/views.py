
from django.shortcuts import render
def display(request):
    rev=''
    if(request.method == "GET"):
        return  render (request,'text.html')
    
    if(request.method =='POST'):
        text=request.POST.get("t1","")
        rev=text[::-1]
    return render(request,"text.html",{"result":rev})
