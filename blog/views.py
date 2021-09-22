from django.shortcuts import render
from django.views import generic
from .forms import ContentForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'

class PostView(generic.FormView):
    template_name = 'post.html'
    from_class = ContentForm