from django.urls import path
from website.modules import views

app_name = 'modules'
urlpatterns = [
    path('', views.index, name='index'),
]
