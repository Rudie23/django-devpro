from django.urls import path
from website.grades import views

app_name = 'grades'

urlpatterns = [
    path('', views.index, name='index'),
]
