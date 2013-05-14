from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from book.settings import EMAIL_HOST_USER

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail(
                    cd['subject'],
                    cd['message'],
                     EMAIL_HOST_USER,
                    ['1156546473@qq.com','swust_oj@163.com'],
                    fail_silently=False
                )
                #print 'send ok'
            except:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/search/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})

from django.template import loader
from django.core.mail import EmailMessage

def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype="html"
    msg.send()

def html_send(request):
    subject="SWUST OJ"
    html_content=loader.render_to_string(
        'send_mail.html',{}
        )
    recipient_list=['1156546473@qq.com']
    send_html_mail(subject, html_content, recipient_list)
    return render(request, 'send_mail.html', {})



