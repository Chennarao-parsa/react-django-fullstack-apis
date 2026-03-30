from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView , UpdateView
from DBapp.models import Employee
# Create your views here.
class Add(View):
    def get(self,request):
        return render(request,'classApp/addition.html')
    def post(self,request):
        v1=int(request.POST['t1'])
        v2=int(request.POST['t2'])
        res=v1+v2
        return render(request,'classApp/addition.html',{'result':res})
class Calculator2(Add):
    def post(self,request):
        v1=int(request.POST['t1'])
        v2=int(request.POST['t2'])
        res=v1*v2
        return render(request,'classApp/addition.html',{'result':res})
class SelectEmployee(ListView):
    model=Employee
    template_name='classApp/select.html'
class InsertEmployee(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'classApp/insert.html'
    success_url = reverse_lazy('selecturl')
class ModifyEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'classApp/update.html'
    success_url = reverse_lazy('selecturl')


