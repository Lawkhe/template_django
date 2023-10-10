from django.shortcuts import render
from django.views.decorators.cache import never_cache

@never_cache
def page(request):
    response = {}       
    return render(request, 'page/content.html', context=response)
