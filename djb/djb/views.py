from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
import datetime

# def hello(request):
#     return HttpResponse("Hello world")

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def hello(request):
    name = 'ysyong'
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def current_datetime(request):
    name = 'ysyong'
    current_date = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context(locals()))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('future_datetime.html')
    html = t.render(Context(locals()))
    return HttpResponse(html)

# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)