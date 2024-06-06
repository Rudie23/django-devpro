from django.urls import path

from website.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
]
