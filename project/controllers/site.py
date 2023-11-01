from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout

@never_cache
def page(request):
    response = {}
    return render(request, 'page/content.html', context=response)

@never_cache
def login(request):
    response = {}       
    return render(request, 'registration/login.html', context=response)

def exit(request):
    logout(request)
    return redirect('login')