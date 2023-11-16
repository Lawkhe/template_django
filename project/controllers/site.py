from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

@never_cache
def page(request):
    response = {}
    return render(request, 'page/content.html', context=response)

@never_cache
def login_view(request):
    response = {}
    if request.method == "POST":
        data = request.POST
        if 'email' in data and data['email'] != '' and 'password' in data and data['password'] != '':
            email = data['email']
            password = data['password']
            try:
                user_val = authenticate(username=email, password=password)
                if user_val is not None:
                    response['status'] = 'success'
                    response['message'] = 'Login exitoso'

                    login(request, user_val)
                    return HttpResponseRedirect('/projects/')
               
            except User.DoesNotExist:
                pass
        response['status'] = 'fail'
        response['message'] = 'El usuario no existe'  
    return render(request, 'registration/login.html', context=response)

def exit(request):
    logout(request)
    return redirect('login')