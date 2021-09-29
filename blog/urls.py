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
    path('comment/<int:pk>/', views.CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', views.ReplyFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', views.reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', views.reply_remove, name='reply_remove'),
]