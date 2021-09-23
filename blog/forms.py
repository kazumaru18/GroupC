from django import forms
from django.forms import fields

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    phonenumber = forms.CharField(label='電話番号', max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['data-sb-validations'] = "required"
        self.fields['name'].widget.attrs['placeholder'] = "Enter your name..."

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['data-sb-validations'] = "required,email" 
        self.fields['email'].widget.attrs['placeholder'] = "Enter your email..."

        self.fields['phonenumber'].widget.attrs['class'] = 'form-control'
        self.fields['phonenumber'].widget.attrs['data-sb-validations'] = "required"
        self.fields['phonenumber'].widget.attrs['placeholder'] = "Enter your phone number..."

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['data-sb-validations'] = "required"
        self.fields['message'].widget.attrs['placeholder'] = "Enter your message here..."

