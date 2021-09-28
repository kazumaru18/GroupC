from django.urls import path
from . import views

app_name = 'sakata'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('post/', views.PostView.as_view(), name="post"),
    path('blog_list/', views.SakataListView.as_view(), name="blog_list"),
    path('blog-detail/<int:pk>/', views.SakataDetailView.as_view(), name="blog_detail"),
    path('blog-create/', views.SakataCreateView.as_view(), name="blog_create"),
    path('blog-update/<int:pk>/', views.SakataUpdateView.as_view(), name="blog_update"),
    path('blog-delete/<int:pk>/', views.SakataDeleteView.as_view(), name="blog_delete"),
]