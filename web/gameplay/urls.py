from django.urls import path

from . import views


app_name = 'gameplay'
urlpatterns = [
    path('', views.main, name='main'),
]