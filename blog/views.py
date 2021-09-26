import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.contrib import messages

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

class ContactView(generic.FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージが送信できました。')
        return super().form_valid(form)
    
class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'


class PostView(generic.TemplateView):
    template_name = 'blog/post.html'