from django.http import HttpResponse
def myview(request):
    return HttpResponse('we are learning Django')
def display(request):
    obj= HttpResponse('we are good students')
    return obj