from django.urls import path

from website.videos import views

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', views.video, name='video'),
    path('', views.index, name='index'),
]
