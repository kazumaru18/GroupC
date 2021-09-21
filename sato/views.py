from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'

class ContactView(generic.TemplateView):
    template_name = 'blog/contact.html'
    
class PostView(generic.TemplateView):
    template_name = 'blog/post.html'