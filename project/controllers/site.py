from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@never_cache
def page(request):
    response = {}
    return render(request, 'page/content.html', context=response)

@never_cache
def login(request):
    response = {}
    if request.method == "POST":
        data = request.POST
        print('data')
        if 'email' in data and data['email'] != '' and 'password' in data and data['password'] != '':
            email = data['email']
            password = data['password']
            try:
                # user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
                # u = User.objects.get(username="john")
                # u.set_password("new password")
                # u.save()

                user_val = authenticate(username=email, password=password)
                print('user_val:___:::::::::::::')
                print(user_val)
                if user_val is not None:
                    response['status'] = 'success'
                    response['message'] = 'Login exitoso'

                    request.session['user'] = {
                        'id': user_val.id,
                        'name': user_val.name,
                    }
                    response['session'] = request.session['user']
                    return HttpResponseRedirect('/projects/')
               
            except User.DoesNotExist:
                pass
        response['status'] = 'fail'
        response['message'] = 'El usuario no existe'  
    return render(request, 'registration/login.html', context=response)

def exit(request):
    logout(request)
    return redirect('login')