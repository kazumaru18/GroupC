from django.urls import path
from . import views

app_name = 'sakata'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('blog-list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog-create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('blog-update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog-delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),
]