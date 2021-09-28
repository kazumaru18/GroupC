import logging
from django.http.response import Http404
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'
    
class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

    template_name = 'blog_detail.html'

class ContactView(generic.FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージが送信できました。')
        return super().form_valid(form)