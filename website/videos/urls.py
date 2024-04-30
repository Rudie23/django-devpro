from django.urls import path

from website.videos import views

app_name = 'videos'
urlpatterns = [
    path('<slug:slug_code>', views.video, name='vimeo'),
]
