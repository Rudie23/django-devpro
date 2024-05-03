from django.urls import path
from website.modules import views

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.detail_of_module, name='detail'),
]
