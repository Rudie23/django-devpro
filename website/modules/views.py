from django.shortcuts import render
from website import facade


# Create your views here.
def detail_of_module(request, slug):
    module = facade.find_module(slug)
    lessons = facade.list_lessons_from_ordered_modules(module)
    return render(request, 'modules/detail_of_module.html', {'module': module, 'lessons': lessons})


def lesson(request, slug):
    lesson = facade.find_lesson(slug)
    return render(request, 'modules/detail_of_lesson.html', {'lesson': lesson})


def list_of_modules_and_lessons(request):
    ctx = {'modules': facade.list_modules_with_lessons()}
    return render(request, 'modules/modules_and_lessons.html', ctx)
