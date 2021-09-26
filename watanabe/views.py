from django.shortcuts import render
from django.views import generic
from . forms import ContactForm
from django.contrib import messages
import logging
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name="index.html"

class ContactView(generic.FormView):
    template_name="contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('watanabe:contact')
    
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self):
        diaries = Blog.objects.filter(user = self.request.user).order_by('-created_at')
        return diaries