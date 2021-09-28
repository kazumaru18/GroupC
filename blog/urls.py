from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('',  views.IndexView.as_view(), name="index"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    # path('diary_create/', views.DiaryCreateView.as_view(), name="diary_create"),
    # path('diary_update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    # path('diary_delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]