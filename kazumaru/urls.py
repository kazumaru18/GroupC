from django.urls import path
from . import views

app_name = 'kazumaru'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('post/', views.post, name="post"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog_list/', views.KazumaruListView.as_view(), name="blog_list"),
    path('blog_detail/<int:pk>/', views.KazumaruDetailView.as_view(), name="blog_detail"),
    path('blog_create/', views.KazumaruCreateView.as_view(), name="blog_create"),
    path('blog_update/<int:pk>/', views.KazumaruUpdateView.as_view(), name="blog_update"),
    path('blog_delete/<int:pk>/', views.KazumaruDeleteView.as_view(), name="blog_delete"),
]
