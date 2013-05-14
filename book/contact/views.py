from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail(
                    cd['subject'],
                    cd['message'],
                     'swust_oj@163.com',
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
