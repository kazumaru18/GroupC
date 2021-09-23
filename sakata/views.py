import logging
# from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm, DiaryCreateForm
from django.urls import reverse_lazy
from django.contrib import messages

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "sakata/index.html"

class AboutView(generic.TemplateView):
    template_name="sakata/about.html"

class ContactView(generic.FormView):
    template_name = "sakata/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('sakata:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class ContactView(generic.TemplateView):
    template_name="sakata/contact.html"

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
class SakataListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries