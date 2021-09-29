import logging
# from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import ContactForm, BlogCreateForm
from django.urls import reverse_lazy
from django.contrib import messages

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class AboutView(generic.TemplateView):
    template_name="about.html"

class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('sakata:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
class BlogListView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 10

    def get_queryset(self):
        diaries = Blog.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    template_name = 'blog_create.html'
    form_class = BlogCreateForm
    success_url = reverse_lazy('sakata:blog_list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        messages.success(self.request, 'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ブログの作成に失敗しました。")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    form_class = BlogCreateForm

    def get_success_url(self):
        return reverse_lazy('sakata:blog_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'ブログを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ブログの更新に失敗しました。")
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('sakata:blog_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "ブログを削除しました。")
        return super().delete(request, *args, **kwargs)