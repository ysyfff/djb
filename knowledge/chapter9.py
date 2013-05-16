
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