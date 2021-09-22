from django.shortcuts import render
from django.views import generic
from . forms import ContactForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name="index.html"

class ContactView(generic.FormView):
    template_name="contact.html"
    form_class = ContactForm
