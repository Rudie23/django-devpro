from django.urls import path
from website.modules import views

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.detail_of_module, name='detail'),
    path('lesson/<slug:slug>', views.lesson, name='lesson'),
    path('', views.list_of_modules_and_lessons, name='index'),
]
