import blog
from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import BooleanField, CharField
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    """"ブログモデル"""
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    title = models.CharField(verbose_name="タイトル", max_length=50)
    content = models.TextField(verbose_name="本文", blank=True, null=True)
    description = models.TextField(verbose_name="説明" ,blank=True)
    img = models.ImageField(verbose_name="イメージ", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    published_at = models.DateField(verbose_name="公開日時", blank=True, null=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Blog"
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def approve(self):
        self.approved = True
        self.save()
    
    def __str__(self):
        return self.text

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text