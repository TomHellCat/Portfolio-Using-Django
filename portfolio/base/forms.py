from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    email = forms.EmailField()
    message = forms.CharField(label='Your name', max_length=200)