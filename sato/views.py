from sato.forms import InquiryForm
from django.shortcuts import render
from django.views import generic
# from .forms import ContactForm
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PostView(generic.TemplateView):
    template_name = 'post.html'


from django.contrib import messages
import logging
from django.urls import reverse_lazy

logger=logging.getLogger(__name__)

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('sato:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


