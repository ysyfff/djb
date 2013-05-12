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

def hello():
    name = 'ysyong'
    time = "now"
    return name, time

def current_datetime(request):
    name, time = hello()
    current_date = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context(locals()))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    name, time = hello()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
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
