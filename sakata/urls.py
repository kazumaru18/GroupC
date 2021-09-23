from django.urls import path
from . import views

app_name = 'sakata'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('post/', views.PostView.as_view(), name="post"),
    path('blog_list/', views.SakataListView.as_view(), name="blog_list"),
]