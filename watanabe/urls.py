from django.urls import path
from . import views

app_name = 'watanabe'

urlpatterns = [
     path('', views.IndexView.as_view() ,name = 'index' ),
     path('contact/', views.ContactView.as_view() ,name = 'contact' ),   
     path('blog_list/', views.DiaryListView.as_view() , name= 'blog_list'), 
]
