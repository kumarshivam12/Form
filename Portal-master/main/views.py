from django.core.mail import send_mail

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm

def get_name(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():



            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})