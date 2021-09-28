from django.contrib import admin
from .models import Blog, ContentImage

# Register your models here.
class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]

admin.site.register(Blog, BlogAdmin)