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


'''
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()


Generic Views of Objects::::::::::::::::::::::::::::::::::::::::::::::::::
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from mysite.books.models import Publisher

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
}

urlpatterns = patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info)
)

'''
In the absence of template_name, though, 
the object_list generic view will infer one from the object’s name. 
In this case, 
the inferred template will be 
"books/publisher_list.html" – the “books” part comes from the name of 
the app that defines the model, 
while the “publisher” bit is just the lowercased version of the model’s name.
'''

{% extends "base.html" %}

{% block content %}
    <h2>Publishers</h2>
    <ul>
        {% for publisher in object_list %}
            <li>{{ publisher.name }}</li>
        {% endfor %}
    </ul>
{% endblock %}

