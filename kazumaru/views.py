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
from .models import Blog
class KazumaruListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self):
        diaries = Blog.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class KazumaruDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'

from .forms import ContactForm, KazumaruCreateForm
class KazumaruCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    template_name = 'blog_create.html'
    form_class = KazumaruCreateForm
    success_url = reverse_lazy('kazumaru:blog_list')

    def form_valid(self, form):
        kazumaru = form.save(commit=False)
        kazumaru.user = self.request.user
        kazumaru.save()
        messages.success(self.request, 'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'ブログの作成に失敗しました。')
        return super().form_invalid(form)
        
class KazumaruUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    form_class = KazumaruCreateForm

    def get_success_url(self):
        return reverse_lazy('kazumaru:blog_detail', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'ブログを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'ブログの更新に失敗しました。')
        return super().form_invalid(form)

class KazumaruDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('kazumaru:blog_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'ブログを削除しました。')
        return super().delete(request, *args, **kwargs)
