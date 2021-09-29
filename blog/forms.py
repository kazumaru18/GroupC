from django import forms
from django.forms import fields
from django.core.mail import EmailMessage
from django.forms import ModelForm, TextInput, Textarea
from blog.models import Blog, Comment, Reply

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
        
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phonenumber = self.cleaned_data['phonenumber']
        message = self.cleaned_data['message']

        subject = "お問い合わせ番号{}".format(phonenumber)
        message = '送信者名：{0}\nメールアドレス：{1}\nメッセージ：\n{2}'.format(name, email, message)
        from_email = 'admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list,)
        message.send()

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'description', 'img', 'published_at')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#以下コメント欄
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '返信内容',
            }),
        }
        labels = {
            'author': ' ',
            'text': ' '
        }