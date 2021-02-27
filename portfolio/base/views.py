from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse

from portfolio.settings import EMAIL_HOST_USER

from django.core.mail import send_mail

from .forms import MessageForm

def index(request):
	return render(request, 'base/index.html')

def aboutme(request):
	return render(request, 'base/aboutme.html')




def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject =  email + " send you an email"
            recipients = ['icecakeinc@gmail.com']
            print(name)
            print(email)
            print(message)
            send_mail(subject, message, EMAIL_HOST_USER, recipients)

    return redirect('/about')




    