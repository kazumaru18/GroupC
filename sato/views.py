from sato.forms import InquiryForm
from django.shortcuts import render
from django.views import generic
# from .forms import ContactForm
# Create your views here.

from .models import Blog
class IndexView(generic.ListView):
    model = Blog
    template_name = 'index.html'
    paginate_by = 3

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

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 5

    # def get_queryset(self):
    #     diaries = Blog.objects.filter(user=self.request.user).order_by('-created_at')
    #     return diaries

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'


from .forms import InquiryForm, BlogCreateForm
class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    template_name = 'blog_create.html'
    form_class = BlogCreateForm
    success_url = reverse_lazy('sato:blog_list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    form_class = BlogCreateForm

    def get_success_url(self):
        return reverse_lazy('sato:blog_detail', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記の更新に失敗しました。')
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('sato:blog_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '日記を削除しました。')
        return super().delete(request, *args, **kwargs)