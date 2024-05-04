from django.shortcuts import render
from website import facade


# Create your views here.
def detail_of_module(request, slug):
    module = facade.find_module(slug)
    lessons = facade.list_lessons_from_ordered_modules(module)
    return render(request, 'modules/detail_of_module.html', {'module': module, 'lessons': lessons})
