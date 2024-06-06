from django.contrib.auth import login
from django.shortcuts import render, redirect
from website.base.forms import RegisterForm
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'base/base.html', {})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form": form})
