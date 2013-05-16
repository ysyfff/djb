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


Making “Friendly” Template Contexts:::::::::::::::::::::::::::::::::::::::::::::::::
'''
You might have noticed that sample publisher list template stores 
all the books in a variable named object_list. 
While this works just fine, 
it isn’t all that “friendly” to template authors: 
they have to “just know” that they’re dealing with books here. 
A better name for that variable would be publisher_list; 
that variable’s content is pretty obvious.
'''
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from mysite.books.models import Publisher

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
    'template_object_name': 'publisher',
}

urlpatterns = patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info)
)
In the template, 
the generic view will append _list to the template_object_name 
to create the variable name representing the list of items.
i.e.:publisher_list


Adding Extra Context::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#bad
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_object_name': 'publisher',
    'extra_context': {'book_list': Book.objects.all()}
}
'''
This would populate a {{ book_list }} variable in the template context. 
This pattern can be used to pass any information down into the template for the generic view. 
It’s very handy.
'''

#good
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_object_name': 'publisher',
    'extra_context': {'book_list': Book.objects.all}
}
'''
Notice the lack of parentheses after Book.objects.all. 
This references the function without actually calling it 
(which the generic view will do later).
'''

Complex Filtering with Wrapper Functions::::::::::::::::::::::::::::::::::::::::::
urlpatterns = patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info),
    (r'^books/(\w+)/$', books_by_publisher),
)

from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from mysite.books.models import Book, Publisher

def books_by_publisher(request, name):

    # Look up the publisher (and raise a 404 if it can't be found).
    publisher = get_object_or_404(Publisher, name__iexact=name)

    # Use the object_list view for the heavy lifting.
    return list_detail.object_list(
        request,
        queryset = Book.objects.filter(publisher=publisher),
        template_name = 'books/books_by_publisher.html',
        template_object_name = 'book',
        extra_context = {'publisher': publisher}
    )



Performing Extra Work::::::::::::::::::::::::::::::::::::::::::::::::::::::
from mysite.books.views import author_detail

urlpatterns = patterns('',
    # ...
    (r'^authors/(?P<author_id>\d+)/$', author_detail),
    # ...
)

import datetime
from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from mysite.books.models import Author

def author_detail(request, author_id):
    # Delegate to the generic view and get an HttpResponse.
    response = list_detail.object_detail(
        request,
        queryset = Author.objects.all(),
        object_id = author_id,
    )

    # Record the last accessed date. We do this *after* the call
    # to object_detail(), not before it, so that this won't be called
    # unless the Author actually exists. (If the author doesn't exist,
    # object_detail() will raise Http404, and we won't reach this point.)
    now = datetime.datetime.now()
    Author.objects.filter(id=author_id).update(last_accessed=now)

    return response



'''
We can use a similar idiom to alter the response returned by the generic view. 
If we wanted to provide a downloadable plain-text version of the list of authors, 
we could use a view like this:
'''
def author_list_plaintext(request):
    response = list_detail.object_list(
        request,
        queryset = Author.objects.all(),
        mimetype = 'text/plain',
        template_name = 'books/author_list.txt'
    )
    response["Content-Disposition"] = "attachment; filename=authors.txt"
    return response




