
#---------------The use of context processors(request)-------------------------#
# from django.template import loader, Context

# def view_1(request):
#     # ...
#     t = loader.get_template('template1.html')
#     c = Context({
#         'app': 'My app',
#         'user': request.user,
#         'ip_address': request.META['REMOTE_ADDR'],
#         'message': 'I am view 1.'
#     })
#     return t.render(c)

# def view_2(request):
#     # ...
#     t = loader.get_template('template2.html')
#     c = Context({
#         'app': 'My app',
#         'user': request.user,
#         'ip_address': request.META['REMOTE_ADDR'],
#         'message': 'I am the second view.'
#     })
#     return t.render(c)

from django.template import loader, RequestContext

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def view_1(request):
    # ...
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am view 1.'},
            processors=[custom_proc])
    return t.render(c)

def view_2(request):
    # ...
    t = loader.get_template('template2.html')
    c = RequestContext(request, {'message': 'I am the second view.'},
            processors=[custom_proc])
    return t.render(c)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

'django.core.context_processors.request'
If this processor is enabled, 
every RequestContext will contain a variable request, 
which is the current HttpRequest object. 
Note that this processor is not enabled by default; 
you have to activate it.

You might want to use this 
if you find your templates needing to access 
attributes of the current HttpRequest such as the IP address:

{{ request.REMOTE_ADDR }}
#---------------The use of context processors(request)-------------------------#


#-------------The strong automatic Html escaping-------------------------------#
By default in Django, every template automatically escapes the output of every variable tag. Specifically, these five characters are escaped:
'''
< is converted to &lt;
> is converted to &gt;
' (single quote) is converted to &#39;
" (double quote) is converted to &quot;
& is converted to &amp;
'''

Again, we stress that this behavior is on by default.
If you’re using Django’s template system, you’re protected.

How to Turn it Off

This will be escaped: {{ data }}
This will not be escaped: {{ data|safe }}

{% autoescape off %}
    Hello {{ name }}
{% endautoescape %}

{% autoescape off %}
    This will not be auto-escaped: {{ data }}.

    Nor this: {{ other_data }}
    {% autoescape on %}
        Auto-escaping applies again: {{ name }}
    {% endautoescape %}
{% endautoescape %}

#-------------The strong automatic Html escaping-------------------------------#


#-------------create a template library----------------------------------------#
Creating a template library is a two-step process:

First, decide which Django application should house the template library. 
If you’ve created an app via manage.py startapp, 
you can put it in there, or you can create another app solely for the template library. 
We’d recommend the latter, because your filters might be useful to you in future projects.

Whichever route you take, make sure to add the app to your INSTALLED_APPS setting. 
We’ll explain this shortly.

Second, create a templatetags directory in the appropriate Django application’s package. 
It should be on the same level as models.py, views.py, and so forth. For example:

books/
    __init__.py
    models.py
    templatetags/
    views.py

Create two empty files in the templatetags directory: 
an __init__.py file (to indicate to Python that this is a package containing Python code) 
and a file that will contain your custom tag/filter definitions. 
The name of the latter file is what you’ll use to load the tags later. 

For example, if your custom tags/filters are in a file called poll_extras.py, 
you’d write the following in a template:
{% load poll_extras %}
#-------------create a template library----------------------------------------#


#-------------Extends the template system--------------------------------------#
'''
THE MEHTOD OF EXTENDING THE TEMPLATE SYSTEM:
IN TEMPLATES's models(such as 'poll_extras.py') WRITE LIKE THIS:
'''
Writing Custom Template Filters:
Custom filters are just Python functions that take one or two arguments:
The value of the variable (input)
The value of the argument, which can have a default value or be left out altogether.

For example, in the filter {{ var|foo:"bar" }},
the filter foo would be passed the contents of the variable var and the argument "bar".

#example
from django import template

register = template.Library()

#function 1
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

#function 2
@register.filter
def lower(value):
    return value.lower()






