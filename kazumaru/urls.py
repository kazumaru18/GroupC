from django.urls import path
from . import views

app_name = 'kazumaru'
urlpatterns = [
    path('', views.index, name="index"),
]