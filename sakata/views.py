import logging
# from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import ContactForm, SakataCreateForm
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

class PostView(generic.TemplateView):
    template_name="sakata/contact.html"

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sakata
class SakataListView(LoginRequiredMixin, generic.ListView):
    model = Sakata
    template_name = 'blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Sakata.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sakata
    template_name = 'diary_detail.html'
    pk_url_kwarg = 'id'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sakata
    template_name = 'sakata_create.html'
    form_class = SakataCreateForm
    success_url = reverse_lazy('sakata:blog_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class SakataUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Sakata
    template_name = 'sakata_update.html'
    form_class = SakataCreateForm

    def get_success_url(self):
        return reverse_lazy('sakata:blog_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Sakata
    template_name = 'sakata_delete.html'
    success_url = reverse_lazy('sakata:blog_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)