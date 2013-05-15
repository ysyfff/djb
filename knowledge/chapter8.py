# # urls.py
# from django.conf.urls.defaults import *
# from mysite import views

# urlpatterns = patterns('',
#     (r'^(foo)/$', views.foobar_view),
#     (r'^(bar)/$', views.foobar_view),
# )

# # views.py
# from django.shortcuts import render
# from mysite.models import MyModel

# def foobar_view(request, url):
#     m_list = MyModel.objects.filter(is_new=True)
#     if url == 'foo':
#         template_name = 'template1.html'
#     elif url == 'bar':
#         template_name = 'template2.html'
#     return render(request, template_name, {'m_list': m_list})

# urls.py
from django.conf.urls.defaults import *
from mysite import views

urlpatterns = patterns('',
    (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
    (r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
)

# views.py
from django.shortcuts import render
from mysite.models import MyModel

def foobar_view(request, template_name):
    m_list = MyModel.objects.filter(is_new=True)
    return render(request, template_name, {'m_list': m_list})

#-----------------The use of extra keyword in urlconf--------------------------#


# urls.py

from django.conf.urls.defaults import *
from mysite import views

urlpatterns = patterns('',
    (r'^blog/$', views.page),
    (r'^blog/page(?P<num>\d+)/$', views.page),
)

# views.py

def page(request, num='1'):
    # Output the appropriate page of blog entries, according to num.
    # ...

'''
Here, both URL patterns point to the same view – views.
page – but the first pattern doesn’t capture anything from the URL. 
If the first pattern matches, 
the page() function will use its default argument for num, '1'. 
If the second pattern matches, 
page() will use whatever num value was captured by the regular expression.
'''
#-----------------The use of default views arguments------------------------#


# # urls.py
# from django.conf.urls.defaults import *
# from mysite import views

# urlpatterns = patterns('',
#     # ...
#     (r'^somepage/$', views.some_page),
#     # ...
# )

# # views.py
# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render

# def some_page(request):
#     if request.method == 'POST':
#         do_something_for_post()
#         return HttpResponseRedirect('/someurl/')
#     elif request.method == 'GET':
#         do_something_for_get()
#         return render(request, 'page.html')
#     else:
#         raise Http404()

# urls.py
from django.conf.urls.defaults import *
from mysite import views

urlpatterns = patterns('',
    # ...
    (r'^somepage/$', views.method_splitter,
        {'GET': views.some_page_get,'POST': views.some_page_post}),
    # ...
)

# views.py
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404

def some_page_get(request):
    assert request.method == 'GET'
    do_something_for_get()
    return render(request, 'page.html')

def some_page_post(request):
    assert request.method == 'POST'
    do_something_for_post()
    return HttpResponseRedirect('/someurl/')

#----------------The use of method_splitter in views------------------------#


