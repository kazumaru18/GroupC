from django.urls import path
from . import views

app_name = 'sato'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('post/', views.PostView.as_view(), name='post'),
]
