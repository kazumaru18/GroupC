from django.urls import path
from . import views

app_name = 'kazumaru'
urlpatterns = [
    path('base/', views.base, name="base"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('post/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),
]