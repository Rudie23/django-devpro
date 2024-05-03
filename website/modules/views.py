from django.shortcuts import render
from website import facade


# Create your views here.
def detail_of_module(request, slug):
    module = facade.find_module(slug=slug)
    return render(request, 'modules/module_detail.html', {'module': module})
