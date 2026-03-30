from django.shortcuts import render
def validation(request):
    msg=''
    uname=''
    if(request.method == 'POST'):
        uname= request.POST.get('t1','')
        if len(uname) < 5:
            msg=' Invalid username can contain atleast 5 chars'
        elif ' ' in uname:
            msg=' Invalid user name not contain any spaces'
        else:
            msg='valid'
    return render(request,'validation.html',{"result":msg})








# Create your views here.
