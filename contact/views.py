from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from forms import ContactForm


def contact_get(request):
    form = ContactForm(initial={'subject': 'Je t\'aime.', 'email': 'jjj@j.com'})
    return render(request, 'contact_form.html', {'form': form})


def contact_post(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        # send_mail(
        #     cd['subject'],
        #     cd['message'],
        #     cd.get('email', 'noreply@example.com'),
        #     ['jin.yuejenny@gmail.com'],
        # )

        return HttpResponseRedirect('thanks')
    else:
        return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')