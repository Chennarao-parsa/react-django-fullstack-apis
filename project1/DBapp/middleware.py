from django.core.exceptions import ValidationError
from django.shortcuts import redirect
class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.method == 'POST' and 'db/insert' in request.path_info:
            if int(request.POST['salary'])<0:
                return redirect('inserturl')

        #validate
        resp=self.get_response(request)
        print("After coming from  the view response")
        return resp


