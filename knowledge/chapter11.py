Using Generic Views:::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from mysite.books.views import about_pages

urlpatterns = patterns('',
    (r'^about/$', direct_to_template, {
        'template': 'about.html'
    }),
    (r'^about/(\w+)/$', about_pages),
)

'''
Though this might seem a bit “magical” at first glance – look, 
a view with no code! –, 
it’s actually exactly the same as the examples in Chapter 8: 
the direct_to_template view simply grabs information 
from the extra-parameters dictionary and uses 
that information when rendering the view.

from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()
'''