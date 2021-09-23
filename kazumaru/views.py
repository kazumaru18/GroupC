from django.shortcuts import render
import logging
from django.contrib import messages
from django.views import generic
from .forms import ContactForm
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name="index.html"

class AboutView(generic.TemplateView):
    template_name="about.html"

def post(request):
    return render(request, 'post.html')

class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('kazumaru:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Kazumaru
class KazumaruListView(LoginRequiredMixin, generic.ListView):
    model = Kazumaru
    template_name = 'blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Kazumaru.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries