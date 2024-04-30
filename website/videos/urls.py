from django.urls import path

from website.videos import views

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', views.video_page, name='vimeo'),
    path('', views.index, name='index'),
]
