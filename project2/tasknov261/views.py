from django.shortcuts import render
def process(request):
    if request.method == 'GET':
        return render(request,'email.html')
    if request.method == 'POST':
        email=request.POST.get('email','')
        msg=''
        if '@' not in email or '.' not in email:
            msg='Invalid email address'
        else:
            a=email.index('@')
            d=email.rindex('.')
            if a < 1:
                msg = 'Invalid email address'
            elif d < a + 2:
                msg = 'Invalid email address'
            elif d + 2 >= len(email):
                msg = 'Invalid email address'
            else:
                msg = 'Valid email address'

        return render(request, 'email.html', {'email': msg})
            
