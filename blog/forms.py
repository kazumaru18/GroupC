from django import forms
from django.forms import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    phonenumber = forms.ChearField(label='電話番号', max_length=30)
    message = forms.ChearField(label="メッセージ", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)